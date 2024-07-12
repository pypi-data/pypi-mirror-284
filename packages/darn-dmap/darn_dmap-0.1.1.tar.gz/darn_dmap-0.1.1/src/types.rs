use crate::error::DmapError;
use indexmap::IndexMap;
use numpy::array::PyArray;
use numpy::ndarray::ArrayD;
use numpy::PyArrayMethods;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::PyAnyMethods;
use pyo3::{Bound, FromPyObject, IntoPy, PyAny, PyObject, PyResult, Python};
use std::cmp::PartialEq;
use std::fmt::{Display, Formatter};
use std::io::Cursor;
use zerocopy::{AsBytes, ByteOrder, FromBytes, LittleEndian};

type Result<T> = std::result::Result<T, DmapError>;

#[derive(Debug, PartialEq)]
pub enum Type {
    Char,
    Short,
    Int,
    Long,
    Uchar,
    Ushort,
    Uint,
    Ulong,
    Float,
    Double,
    String,
}
impl Display for Type {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Char => write!(f, "CHAR"),
            Self::Short => write!(f, "SHORT"),
            Self::Int => write!(f, "INT"),
            Self::Float => write!(f, "FLOAT"),
            Self::Double => write!(f, "DOUBLE"),
            Self::String => write!(f, "STRING"),
            Self::Long => write!(f, "LONG"),
            Self::Uchar => write!(f, "UCHAR"),
            Self::Ushort => write!(f, "USHORT"),
            Self::Uint => write!(f, "UINT"),
            Self::Ulong => write!(f, "ULONG"),
        }
    }
}
impl Type {
    fn from_key(key: i8) -> Result<Self> {
        let data = match key {
            1 => Self::Char,
            2 => Self::Short,
            3 => Self::Int,
            10 => Self::Long,
            16 => Self::Uchar,
            17 => Self::Ushort,
            18 => Self::Uint,
            19 => Self::Ulong,
            4 => Self::Float,
            8 => Self::Double,
            9 => Self::String,
            x => Err(DmapError::KeyError(x))?,
        };
        Ok(data)
    }
    fn key(&self) -> i8 {
        match self {
            Self::Char => 1,
            Self::Short => 2,
            Self::Int => 3,
            Self::Long => 10,
            Self::Uchar => 16,
            Self::Ushort => 17,
            Self::Uint => 18,
            Self::Ulong => 19,
            Self::Float => 4,
            Self::Double => 8,
            Self::String => 9,
        }
    }

    fn size(&self) -> usize {
        match self {
            Self::Char => 1,
            Self::Short => 2,
            Self::Int => 4,
            Self::Long => 8,
            Self::Uchar => 1,
            Self::Ushort => 2,
            Self::Uint => 4,
            Self::Ulong => 8,
            Self::Float => 4,
            Self::Double => 8,
            Self::String => 0,
        }
    }
}
/// Enum of the different data types supported by the DMAP format.
#[derive(Debug, Clone, PartialEq, FromPyObject)]
#[repr(C)]
pub enum DmapScalar {
    Char(i8),
    Short(i16),
    Int(i32),
    Long(i64),
    Uchar(u8),
    Ushort(u16),
    Uint(u32),
    Ulong(u64),
    Float(f32),
    Double(f64),
    String(String),
}
impl DmapScalar {
    pub(crate) fn get_type(&self) -> Type {
        match self {
            Self::Char(_) => Type::Char,
            Self::Short(_) => Type::Short,
            Self::Int(_) => Type::Int,
            Self::Long(_) => Type::Long,
            Self::Uchar(_) => Type::Uchar,
            Self::Ushort(_) => Type::Ushort,
            Self::Uint(_) => Type::Uint,
            Self::Ulong(_) => Type::Ulong,
            Self::Float(_) => Type::Float,
            Self::Double(_) => Type::Double,
            Self::String(_) => Type::String,
        }
    }
    pub(crate) fn cast_as(&self, new_type: &Type) -> Result<Self> {
        match new_type {
            Type::Char => Ok(Self::Char(i8::try_from(self)?)),
            Type::Short => Ok(Self::Short(i16::try_from(self)?)),
            Type::Int => Ok(Self::Int(i32::try_from(self)?)),
            Type::Long => Ok(Self::Long(i64::try_from(self)?)),
            Type::Uchar => Ok(Self::Uchar(u8::try_from(self)?)),
            Type::Ushort => Ok(Self::Ushort(u16::try_from(self)?)),
            Type::Uint => Ok(Self::Uint(u32::try_from(self)?)),
            Type::Ulong => Ok(Self::Ulong(u64::try_from(self)?)),
            Type::Float => Ok(Self::Float(f32::try_from(self)?)),
            Type::Double => Ok(Self::Double(f64::try_from(self)?)),
            Type::String => Err(DmapError::ScalarError(
                "Unable to cast value to String".to_string(),
            )),
        }
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes: Vec<u8> = DmapType::as_bytes(&self.get_type().key()).to_vec();
        let mut data_bytes: Vec<u8> = match self {
            Self::Char(x) => DmapType::as_bytes(x),
            Self::Short(x) => DmapType::as_bytes(x),
            Self::Int(x) => DmapType::as_bytes(x),
            Self::Long(x) => DmapType::as_bytes(x),
            Self::Uchar(x) => DmapType::as_bytes(x),
            Self::Ushort(x) => DmapType::as_bytes(x),
            Self::Uint(x) => DmapType::as_bytes(x),
            Self::Ulong(x) => DmapType::as_bytes(x),
            Self::Float(x) => DmapType::as_bytes(x),
            Self::Double(x) => DmapType::as_bytes(x),
            Self::String(x) => DmapType::as_bytes(x),
        };
        bytes.append(&mut data_bytes);
        bytes
    }
}
impl Display for DmapScalar {
    fn fmt(&self, f: &mut Formatter) -> std::fmt::Result {
        match self {
            Self::Char(x) => write!(f, "CHAR {x}"),
            Self::Short(x) => write!(f, "SHORT {x}"),
            Self::Int(x) => write!(f, "INT {x}"),
            Self::Float(x) => write!(f, "FLOAT {x}"),
            Self::Double(x) => write!(f, "DOUBLE {x}"),
            Self::String(x) => write!(f, "STRING {x}"),
            Self::Long(x) => write!(f, "LONG {x}"),
            Self::Uchar(x) => write!(f, "UCHAR {x}"),
            Self::Ushort(x) => write!(f, "USHORT {x}"),
            Self::Uint(x) => write!(f, "UINT {x}"),
            Self::Ulong(x) => write!(f, "ULONG {x}"),
        }
    }
}
impl IntoPy<PyObject> for DmapScalar {
    fn into_py(self, py: Python<'_>) -> PyObject {
        match self {
            Self::Char(x) => x.into_py(py),
            Self::Short(x) => x.into_py(py),
            Self::Int(x) => x.into_py(py),
            Self::Long(x) => x.into_py(py),
            Self::Uchar(x) => x.into_py(py),
            Self::Ushort(x) => x.into_py(py),
            Self::Uint(x) => x.into_py(py),
            Self::Ulong(x) => x.into_py(py),
            Self::Float(x) => x.into_py(py),
            Self::Double(x) => x.into_py(py),
            Self::String(x) => x.into_py(py),
        }
    }
}

#[derive(Clone, Debug, PartialEq)]
pub enum DmapVec {
    Char(ArrayD<i8>),
    Short(ArrayD<i16>),
    Int(ArrayD<i32>),
    Long(ArrayD<i64>),
    Uchar(ArrayD<u8>),
    Ushort(ArrayD<u16>),
    Uint(ArrayD<u32>),
    Ulong(ArrayD<u64>),
    Float(ArrayD<f32>),
    Double(ArrayD<f64>),
}
impl DmapVec {
    pub(crate) fn get_type(&self) -> Type {
        match self {
            DmapVec::Char(_) => Type::Char,
            DmapVec::Short(_) => Type::Short,
            DmapVec::Int(_) => Type::Int,
            DmapVec::Long(_) => Type::Long,
            DmapVec::Uchar(_) => Type::Uchar,
            DmapVec::Ushort(_) => Type::Ushort,
            DmapVec::Uint(_) => Type::Uint,
            DmapVec::Ulong(_) => Type::Ulong,
            DmapVec::Float(_) => Type::Float,
            DmapVec::Double(_) => Type::Double,
        }
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes: Vec<u8> = DmapType::as_bytes(&self.get_type().key()).to_vec();
        match self {
            DmapVec::Char(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Short(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Int(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Long(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Uchar(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Ushort(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Uint(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Ulong(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Float(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
            DmapVec::Double(x) => {
                bytes.extend((x.ndim() as i32).to_le_bytes());
                for &dim in x.shape().iter().rev() {
                    bytes.extend((dim as i32).to_le_bytes());
                }
                for y in x.iter() {
                    bytes.append(&mut DmapType::as_bytes(y).to_vec());
                }
            }
        };
        bytes
    }
}
impl IntoPy<PyObject> for DmapVec {
    fn into_py(self, py: Python<'_>) -> PyObject {
        match self {
            DmapVec::Char(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Short(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Int(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Long(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Uchar(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Ushort(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Uint(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Ulong(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Float(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
            DmapVec::Double(x) => PyObject::from(PyArray::from_owned_array_bound(py, x)),
        }
    }
}
impl<'py> FromPyObject<'py> for DmapVec {
    fn extract_bound(ob: &Bound<'py, PyAny>) -> PyResult<Self> {
        if let Ok(x) = ob.downcast::<PyArray<u8, _>>() {
            Ok(DmapVec::Uchar(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<u16, _>>() {
            Ok(DmapVec::Ushort(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<u32, _>>() {
            Ok(DmapVec::Uint(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<u64, _>>() {
            Ok(DmapVec::Ulong(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<i8, _>>() {
            Ok(DmapVec::Char(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<i16, _>>() {
            Ok(DmapVec::Short(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<i32, _>>() {
            Ok(DmapVec::Int(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<i64, _>>() {
            Ok(DmapVec::Long(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<f32, _>>() {
            Ok(DmapVec::Float(x.to_owned_array()))
        } else if let Ok(x) = ob.downcast::<PyArray<f64, _>>() {
            Ok(DmapVec::Double(x.to_owned_array()))
        } else {
            Err(PyValueError::new_err("Could not extract vector"))
        }
    }
}

#[derive(Debug, Clone, PartialEq, FromPyObject)]
#[repr(C)]
pub enum DmapField {
    Scalar(DmapScalar),
    Vector(DmapVec),
}
impl DmapField {
    pub fn as_bytes(&self) -> Vec<u8> {
        match self {
            Self::Scalar(x) => x.as_bytes(),
            Self::Vector(x) => x.as_bytes(),
        }
    }
}
impl IntoPy<PyObject> for DmapField {
    fn into_py(self, py: Python<'_>) -> PyObject {
        match self {
            DmapField::Scalar(x) => x.into_py(py),
            DmapField::Vector(x) => x.into_py(py),
        }
    }
}

/// Trait for types that can be stored in DMAP files
pub trait DmapType: std::fmt::Debug {
    fn size() -> usize
    where
        Self: Sized;
    fn as_bytes(&self) -> Vec<u8>;
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized;
    fn get_dmap_key() -> u8
    where
        Self: Sized;
    fn dmap_type(&self) -> Type;
}
impl DmapType for i8 {
    fn size() -> usize {
        1
    }
    fn get_dmap_key() -> u8 {
        1
    }
    fn as_bytes(&self) -> Vec<u8> {
        AsBytes::as_bytes(self).to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Char
    }
}
impl DmapType for i16 {
    fn size() -> usize {
        2
    }
    fn get_dmap_key() -> u8 {
        2
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 2];
        LittleEndian::write_i16(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Short
    }
}
impl DmapType for i32 {
    fn size() -> usize {
        4
    }
    fn get_dmap_key() -> u8 {
        3
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 4];
        LittleEndian::write_i32(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Int
    }
}
impl DmapType for i64 {
    fn size() -> usize {
        8
    }
    fn get_dmap_key() -> u8 {
        10
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 8];
        LittleEndian::write_i64(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Long
    }
}
impl DmapType for u8 {
    fn size() -> usize {
        1
    }
    fn get_dmap_key() -> u8 {
        16
    }
    fn as_bytes(&self) -> Vec<u8> {
        AsBytes::as_bytes(self).to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Uchar
    }
}
impl DmapType for u16 {
    fn size() -> usize {
        2
    }
    fn get_dmap_key() -> u8 {
        17
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 2];
        LittleEndian::write_u16(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Ushort
    }
}
impl DmapType for u32 {
    fn size() -> usize {
        4
    }
    fn get_dmap_key() -> u8 {
        18
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 4];
        LittleEndian::write_u32(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Uint
    }
}
impl DmapType for u64 {
    fn size() -> usize {
        8
    }
    fn get_dmap_key() -> u8 {
        19
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 8];
        LittleEndian::write_u64(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Ulong
    }
}
impl DmapType for f32 {
    fn size() -> usize {
        4
    }
    fn get_dmap_key() -> u8 {
        4
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 4];
        LittleEndian::write_f32(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Float
    }
}
impl DmapType for f64 {
    fn size() -> usize {
        8
    }
    fn get_dmap_key() -> u8 {
        8
    }
    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = [0; 8];
        LittleEndian::write_f64(&mut bytes, *self);
        bytes.to_vec()
    }
    fn from_bytes(bytes: &[u8]) -> Result<Self>
    where
        Self: Sized,
    {
        Self::read_from(bytes).ok_or(DmapError::CorruptDmapError("Unable to interpret bytes"))
    }
    fn dmap_type(&self) -> Type {
        Type::Double
    }
}
impl DmapType for String {
    fn size() -> usize {
        0
    }

    fn as_bytes(&self) -> Vec<u8> {
        let mut bytes = self.as_bytes().to_vec();
        bytes.push(0); // null-terminate
        bytes
    }

    fn from_bytes(bytes: &[u8]) -> Result<Self> {
        let data = String::from_utf8(bytes.to_owned())
            .map_err(|_| DmapError::ScalarError(format!("Cannot convert bytes to String")))?;
        Ok(data.trim_end_matches(char::from(0)).to_string())
    }
    fn get_dmap_key() -> u8 {
        9
    }
    fn dmap_type(&self) -> Type {
        Type::String
    }
}
impl TryFrom<&DmapScalar> for u8 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as u8),
            DmapScalar::Short(x) => Ok(x.clone() as u8),
            DmapScalar::Int(x) => Ok(x.clone() as u8),
            DmapScalar::Long(x) => Ok(x.clone() as u8),
            DmapScalar::Uchar(x) => Ok(x.clone()),
            DmapScalar::Ushort(x) => Ok(x.clone() as u8),
            DmapScalar::Uint(x) => Ok(x.clone() as u8),
            DmapScalar::Ulong(x) => Ok(x.clone() as u8),
            DmapScalar::Float(x) => Ok(x.clone() as u8),
            DmapScalar::Double(x) => Ok(x.clone() as u8),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to u8"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for u16 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as u16),
            DmapScalar::Short(x) => Ok(x.clone() as u16),
            DmapScalar::Int(x) => Ok(x.clone() as u16),
            DmapScalar::Long(x) => Ok(x.clone() as u16),
            DmapScalar::Uchar(x) => Ok(x.clone() as u16),
            DmapScalar::Ushort(x) => Ok(x.clone()),
            DmapScalar::Uint(x) => Ok(x.clone() as u16),
            DmapScalar::Ulong(x) => Ok(x.clone() as u16),
            DmapScalar::Float(x) => Ok(x.clone() as u16),
            DmapScalar::Double(x) => Ok(x.clone() as u16),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to u16"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for u32 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as u32),
            DmapScalar::Short(x) => Ok(x.clone() as u32),
            DmapScalar::Int(x) => Ok(x.clone() as u32),
            DmapScalar::Long(x) => Ok(x.clone() as u32),
            DmapScalar::Uchar(x) => Ok(x.clone() as u32),
            DmapScalar::Ushort(x) => Ok(x.clone() as u32),
            DmapScalar::Uint(x) => Ok(x.clone()),
            DmapScalar::Ulong(x) => Ok(x.clone() as u32),
            DmapScalar::Float(x) => Ok(x.clone() as u32),
            DmapScalar::Double(x) => Ok(x.clone() as u32),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to u32"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for u64 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as u64),
            DmapScalar::Short(x) => Ok(x.clone() as u64),
            DmapScalar::Int(x) => Ok(x.clone() as u64),
            DmapScalar::Long(x) => Ok(x.clone() as u64),
            DmapScalar::Uchar(x) => Ok(x.clone() as u64),
            DmapScalar::Ushort(x) => Ok(x.clone() as u64),
            DmapScalar::Uint(x) => Ok(x.clone() as u64),
            DmapScalar::Ulong(x) => Ok(x.clone()),
            DmapScalar::Float(x) => Ok(x.clone() as u64),
            DmapScalar::Double(x) => Ok(x.clone() as u64),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to u64"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for i8 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone()),
            DmapScalar::Short(x) => Ok(x.clone() as i8),
            DmapScalar::Int(x) => Ok(x.clone() as i8),
            DmapScalar::Long(x) => Ok(x.clone() as i8),
            DmapScalar::Uchar(x) => Ok(x.clone() as i8),
            DmapScalar::Ushort(x) => Ok(x.clone() as i8),
            DmapScalar::Uint(x) => Ok(x.clone() as i8),
            DmapScalar::Ulong(x) => Ok(x.clone() as i8),
            DmapScalar::Float(x) => Ok(x.clone() as i8),
            DmapScalar::Double(x) => Ok(x.clone() as i8),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to i8"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for i16 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as i16),
            DmapScalar::Short(x) => Ok(x.clone()),
            DmapScalar::Int(x) => Ok(x.clone() as i16),
            DmapScalar::Long(x) => Ok(x.clone() as i16),
            DmapScalar::Uchar(x) => Ok(x.clone() as i16),
            DmapScalar::Ushort(x) => Ok(x.clone() as i16),
            DmapScalar::Uint(x) => Ok(x.clone() as i16),
            DmapScalar::Ulong(x) => Ok(x.clone() as i16),
            DmapScalar::Float(x) => Ok(x.clone() as i16),
            DmapScalar::Double(x) => Ok(x.clone() as i16),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to i16"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for i32 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as i32),
            DmapScalar::Short(x) => Ok(x.clone() as i32),
            DmapScalar::Int(x) => Ok(x.clone()),
            DmapScalar::Long(x) => Ok(x.clone() as i32),
            DmapScalar::Uchar(x) => Ok(x.clone() as i32),
            DmapScalar::Ushort(x) => Ok(x.clone() as i32),
            DmapScalar::Uint(x) => Ok(x.clone() as i32),
            DmapScalar::Ulong(x) => Ok(x.clone() as i32),
            DmapScalar::Float(x) => Ok(x.clone() as i32),
            DmapScalar::Double(x) => Ok(x.clone() as i32),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to i32"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for i64 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as i64),
            DmapScalar::Short(x) => Ok(x.clone() as i64),
            DmapScalar::Int(x) => Ok(x.clone() as i64),
            DmapScalar::Long(x) => Ok(x.clone()),
            DmapScalar::Uchar(x) => Ok(x.clone() as i64),
            DmapScalar::Ushort(x) => Ok(x.clone() as i64),
            DmapScalar::Uint(x) => Ok(x.clone() as i64),
            DmapScalar::Ulong(x) => Ok(x.clone() as i64),
            DmapScalar::Float(x) => Ok(x.clone() as i64),
            DmapScalar::Double(x) => Ok(x.clone() as i64),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to i64"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for f32 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as f32),
            DmapScalar::Short(x) => Ok(x.clone() as f32),
            DmapScalar::Int(x) => Ok(x.clone() as f32),
            DmapScalar::Long(x) => Ok(x.clone() as f32),
            DmapScalar::Uchar(x) => Ok(x.clone() as f32),
            DmapScalar::Ushort(x) => Ok(x.clone() as f32),
            DmapScalar::Uint(x) => Ok(x.clone() as f32),
            DmapScalar::Ulong(x) => Ok(x.clone() as f32),
            DmapScalar::Float(x) => Ok(x.clone()),
            DmapScalar::Double(x) => Ok(x.clone() as f32),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to f32"
            ))),
        }
    }
}
impl TryFrom<&DmapScalar> for f64 {
    type Error = DmapError;
    fn try_from(value: &DmapScalar) -> std::result::Result<Self, Self::Error> {
        match value {
            DmapScalar::Char(x) => Ok(x.clone() as f64),
            DmapScalar::Short(x) => Ok(x.clone() as f64),
            DmapScalar::Int(x) => Ok(x.clone() as f64),
            DmapScalar::Long(x) => Ok(x.clone() as f64),
            DmapScalar::Uchar(x) => Ok(x.clone() as f64),
            DmapScalar::Ushort(x) => Ok(x.clone() as f64),
            DmapScalar::Uint(x) => Ok(x.clone() as f64),
            DmapScalar::Ulong(x) => Ok(x.clone() as f64),
            DmapScalar::Float(x) => Ok(x.clone() as f64),
            DmapScalar::Double(x) => Ok(x.clone()),
            DmapScalar::String(x) => Err(DmapError::ScalarError(format!(
                "Unable to convert {x} to f64"
            ))),
        }
    }
}
pub fn check_scalar(
    fields: &mut IndexMap<String, DmapField>,
    name: &str,
    expected_type: Type,
) -> Result<()> {
    match fields.get(name) {
        Some(&DmapField::Scalar(ref data)) if data.get_type() == expected_type => Ok(()),
        Some(&DmapField::Scalar(ref data)) => Err(DmapError::ScalarError(format!(
            "{name} is of type {}, expected {}",
            data.get_type(),
            expected_type
        ))),
        Some(_) => Err(DmapError::ScalarError(format!("{name} is a vector field"))),
        None => Err(DmapError::ScalarError(format!("{name} is not in record"))),
    }
}

pub fn check_scalar_opt(
    fields: &mut IndexMap<String, DmapField>,
    name: &str,
    expected_type: Type,
) -> Result<()> {
    match fields.get(name) {
        Some(&DmapField::Scalar(ref data)) if data.get_type() == expected_type => Ok(()),
        Some(&DmapField::Scalar(ref data)) => Err(DmapError::ScalarError(format!(
            "{name} is of type {}, expected {}",
            data.get_type(),
            expected_type
        ))),
        Some(_) => Err(DmapError::ScalarError(format!("{name} is a vector field"))),
        None => Ok(()),
    }
}

pub fn check_vector(
    fields: &mut IndexMap<String, DmapField>,
    name: &str,
    expected_type: Type,
) -> Result<()> {
    match fields.get(name) {
        Some(DmapField::Vector(data)) if data.get_type() != expected_type => {
            Err(DmapError::VectorError(format!(
                "{name} is of type {}, expected {}",
                data.get_type(),
                expected_type
            )))
        }
        Some(DmapField::Scalar(_)) => {
            Err(DmapError::VectorError(format!("{name} is a scalar field")))
        }
        None => Err(DmapError::VectorError(format!("{name} not in record"))),
        _ => Ok(()),
    }
}

pub fn check_vector_opt(
    fields: &mut IndexMap<String, DmapField>,
    name: &str,
    expected_type: Type,
) -> Result<()> {
    match fields.get(name) {
        Some(DmapField::Vector(data)) if data.get_type() != expected_type => {
            Err(DmapError::VectorError(format!(
                "{name} is of type {}, expected {}",
                data.get_type(),
                expected_type
            )))
        }
        Some(DmapField::Scalar(_)) => {
            Err(DmapError::VectorError(format!("{name} is a scalar field")))
        }
        _ => Ok(()),
    }
}

/// Reads a scalar starting from cursor position
pub(crate) fn parse_scalar(cursor: &mut Cursor<Vec<u8>>) -> Result<(String, DmapField)> {
    let _mode = 6;
    let name = read_data::<String>(cursor).map_err(|e| {
        DmapError::ScalarError(format!(
            "Invalid scalar name, byte {}: {e}",
            cursor.position()
        ))
    })?;
    let data_type_key = match read_data::<i8>(cursor) {
        Err(e) => Err(DmapError::ScalarError(format!(
            "Invalid data type for field '{name}', byte {}: {e}",
            cursor.position() - i8::size() as u64
        )))?,
        Ok(x) => Type::from_key(x).map_err(|e| {
            DmapError::ScalarError(format!(
                "Field {name}: {e}, byte {}",
                cursor.position() - i8::size() as u64
            ))
        })?,
    };

    let data: DmapScalar = match data_type_key {
        Type::Char => DmapScalar::Char(read_data::<i8>(cursor)?),
        Type::Short => DmapScalar::Short(read_data::<i16>(cursor)?),
        Type::Int => DmapScalar::Int(read_data::<i32>(cursor)?),
        Type::Long => DmapScalar::Long(read_data::<i64>(cursor)?),
        Type::Uchar => DmapScalar::Uchar(read_data::<u8>(cursor)?),
        Type::Ushort => DmapScalar::Ushort(read_data::<u16>(cursor)?),
        Type::Uint => DmapScalar::Uint(read_data::<u32>(cursor)?),
        Type::Ulong => DmapScalar::Ulong(read_data::<u64>(cursor)?),
        Type::Float => DmapScalar::Float(read_data::<f32>(cursor)?),
        Type::Double => DmapScalar::Double(read_data::<f64>(cursor)?),
        Type::String => DmapScalar::String(read_data::<String>(cursor)?),
    };

    Ok((name, DmapField::Scalar(data)))
}

/// Reads a vector starting from cursor position
pub(crate) fn parse_vector(
    cursor: &mut Cursor<Vec<u8>>,
    record_size: i32,
) -> Result<(String, DmapField)> {
    let _mode = 7;
    let name = read_data::<String>(cursor).map_err(|e| {
        DmapError::VectorError(format!(
            "Invalid vector name, byte {}: {e}",
            cursor.position()
        ))
    })?;
    let data_type_key = read_data::<i8>(cursor).map_err(|e| {
        DmapError::VectorError(format!(
            "Invalid data type for field '{name}', byte {}: {e}",
            cursor.position() - i8::size() as u64
        ))
    })?;

    let data_type = Type::from_key(data_type_key)?;

    let vector_dimension = read_data::<i32>(cursor)?;
    if vector_dimension > record_size {
        return Err(DmapError::VectorError(format!(
            "Parsed number of vector dimensions {} for field '{}' at byte {} are larger \
            than record size {}",
            vector_dimension,
            name,
            cursor.position() - i32::size() as u64,
            record_size
        )));
    } else if vector_dimension <= 0 {
        return Err(DmapError::VectorError(format!(
            "Parsed number of vector dimensions {} for field '{}' at byte {} are zero or \
            negative",
            vector_dimension,
            name,
            cursor.position() - i32::size() as u64,
        )));
    }

    let mut dimensions: Vec<usize> = vec![];
    let mut total_elements = 1;
    for _ in 0..vector_dimension {
        let dim = read_data::<i32>(cursor)?;
        if dim <= 0 && name != "slist" {
            return Err(DmapError::VectorError(format!(
                "Vector dimension {} at byte {} is zero or negative for field '{}'",
                dim,
                cursor.position() - i32::size() as u64,
                name
            )));
        } else if dim > record_size {
            return Err(DmapError::VectorError(format!(
                "Vector dimension {} at byte {} for field '{}' exceeds record size {} ",
                dim,
                cursor.position() - i32::size() as u64,
                name,
                record_size,
            )));
        }
        dimensions.push(dim as u32 as usize);
        total_elements *= dim;
    }
    dimensions = dimensions.into_iter().rev().collect(); // reverse the dimensions, stored in column-major order
    if total_elements * data_type.size() as i32 > record_size {
        return Err(DmapError::VectorError(format!(
            "Vector size {} starting at byte {} for field '{}' exceeds record size {}",
            total_elements * data_type.size() as i32,
            cursor.position() - vector_dimension as u64 * i32::size() as u64,
            name,
            record_size
        )));
    }

    let vector: DmapVec = match data_type {
        Type::Char => DmapVec::Char(
            ArrayD::from_shape_vec(dimensions, read_vector::<i8>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Short => DmapVec::Short(
            ArrayD::from_shape_vec(dimensions, read_vector::<i16>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Int => DmapVec::Int(
            ArrayD::from_shape_vec(dimensions, read_vector::<i32>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Long => DmapVec::Long(
            ArrayD::from_shape_vec(dimensions, read_vector::<i64>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Uchar => DmapVec::Uchar(
            ArrayD::from_shape_vec(dimensions, read_vector::<u8>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Ushort => DmapVec::Ushort(
            ArrayD::from_shape_vec(dimensions, read_vector::<u16>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Uint => DmapVec::Uint(
            ArrayD::from_shape_vec(dimensions, read_vector::<u32>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Ulong => DmapVec::Ulong(
            ArrayD::from_shape_vec(dimensions, read_vector::<u64>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Float => DmapVec::Float(
            ArrayD::from_shape_vec(dimensions, read_vector::<f32>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        Type::Double => DmapVec::Double(
            ArrayD::from_shape_vec(dimensions, read_vector::<f64>(cursor, total_elements)?)
                .map_err(|e| {
                    DmapError::VectorError(format!("Could not read in vector field {name}: {e}"))
                })?,
        ),
        _ => {
            return Err(DmapError::VectorError(format!(
                "Invalid type {} for DMAP vector {}",
                data_type, name
            )))
        }
    };

    Ok((name, DmapField::Vector(vector)))
}

fn read_vector<T: DmapType>(cursor: &mut Cursor<Vec<u8>>, num_elements: i32) -> Result<Vec<T>> {
    let mut data: Vec<T> = vec![];
    for _ in 0..num_elements {
        data.push(read_data::<T>(cursor)?);
    }
    Ok(data)
}

/// Reads a singular value of type T starting from cursor position
pub(crate) fn read_data<T: DmapType>(cursor: &mut Cursor<Vec<u8>>) -> Result<T> {
    let position = cursor.position() as usize;
    let stream = cursor.get_mut();

    if position > stream.len() {
        return Err(DmapError::CorruptDmapError("Cursor extends out of buffer"));
    }
    if stream.len() - position < T::size() {
        return Err(DmapError::CorruptDmapError(
            "Byte offsets into buffer are not properly aligned",
        ));
    }

    let data_size = match T::size() {
        0 => {
            // String type
            let mut byte_counter = 0;
            while stream[position + byte_counter] != 0 {
                byte_counter += 1;
                if position + byte_counter >= stream.len() {
                    return Err(DmapError::CorruptDmapError(
                        "String is improperly terminated",
                    ));
                }
            }
            byte_counter + 1
        }
        x => x,
    };
    let data: &[u8] = &stream[position..position + data_size];
    let parsed_data = T::from_bytes(data)?;

    cursor.set_position({ position + data_size } as u64);

    Ok(parsed_data)
}
