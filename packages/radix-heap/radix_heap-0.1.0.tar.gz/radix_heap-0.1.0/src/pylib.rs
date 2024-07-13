use ordered_float::NotNan;
use pyo3::prelude::*;
use radix_heap::RadixHeapMap;

#[pyclass(subclass)]
pub struct RadixHeapLike {

}

#[pyclass(name = "RadixMaxHeapInt", extends = RadixHeapLike)]
pub struct PyRadixMaxHeapInt {
    pub inner: RadixHeapMap<i64, PyObject>,
}

#[pymethods]
impl PyRadixMaxHeapInt {
    #[new]
    fn new() -> (Self, RadixHeapLike) {
        (PyRadixMaxHeapInt {
            inner: RadixHeapMap::new(),
        }, RadixHeapLike {})
    }

    pub fn push(&mut self, value: i64, item: PyObject) {
        self.inner.push(value, item);
    }

    pub fn pop(&mut self) -> PyResult<PyObject> {
        match self.inner.pop() {
            Some((_, item)) => Ok(item),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn pop_with_key(&mut self) -> PyResult<(i64, PyObject)> {
        match self.inner.pop() {
            Some((value, item)) => Ok((value, item)),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn top(&self) -> Option<i64> {
        match self.inner.top() {
            Some(k) => Some(k),
            None => None,
        }
    }

    pub fn clear(&mut self) {
        self.inner.clear();
    }

    pub fn __len__(&self) -> usize {
        self.inner.len()
    }
}

#[pyclass(name = "RadixMinHeapInt", extends = RadixHeapLike)]
pub struct PyRadixMinHeapInt {
    pub inner: RadixHeapMap<i64, PyObject>,
}

#[pymethods]
impl PyRadixMinHeapInt {
    #[new]
    fn new() -> (Self, RadixHeapLike) {
        (PyRadixMinHeapInt {
            inner: RadixHeapMap::new(),
        }, RadixHeapLike {})
    }

    pub fn push(&mut self, value: i64, item: PyObject) {
        self.inner.push(-value, item);
    }

    pub fn pop(&mut self) -> PyResult<PyObject> {
        match self.inner.pop() {
            Some((_, item)) => Ok(item),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn pop_with_key(&mut self) -> PyResult<(i64, PyObject)> {
        match self.inner.pop() {
            Some((value, item)) => Ok((-value, item)),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn top(&self) -> Option<i64> {
        match self.inner.top() {
            Some(k) => Some(-k),
            None => None,
        }
    }

    pub fn clear(&mut self) {
        self.inner.clear();
    }

    pub fn __len__(&self) -> usize {
        self.inner.len()
    }
}

#[pyclass(name = "RadixMaxHeap", extends = RadixHeapLike)]
pub struct PyRadixMaxHeap {
    pub inner: RadixHeapMap<NotNan<f64>, PyObject>,
}

#[pymethods]
impl PyRadixMaxHeap {
    #[new]
    fn new() -> (Self, RadixHeapLike) {
        (PyRadixMaxHeap {
            inner: RadixHeapMap::new(),
        }, RadixHeapLike {})
    }

    pub fn push(&mut self, value: f64, item: PyObject) -> PyResult<()> {
        match NotNan::new(value) {
            Ok(v) => {
                self.inner.push(v, item);
                Ok(())
            }
            Err(_) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "value is NaN",
            )),
        }
    }

    pub fn pop(&mut self) -> PyResult<PyObject> {
        match self.inner.pop() {
            Some((_, item)) => Ok(item),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn pop_with_key(&mut self) -> PyResult<(f64, PyObject)> {
        match self.inner.pop() {
            Some((value, item)) => Ok((value.into_inner(), item)),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn top(&self) -> Option<f64> {
        match self.inner.top() {
            Some(k) => Some(k.into_inner()),
            None => None,
        }
    }

    pub fn clear(&mut self) {
        self.inner.clear();
    }

    pub fn __len__(&self) -> usize {
        self.inner.len()
    }
}

#[pyclass(name = "RadixMinHeap", extends = RadixHeapLike)]
pub struct PyRadixMinHeap {
    pub inner: RadixHeapMap<NotNan<f64>, PyObject>,
}

#[pymethods]
impl PyRadixMinHeap {
    #[new]
    fn new() -> (Self, RadixHeapLike) {
        (PyRadixMinHeap {
            inner: RadixHeapMap::new(),
        }, RadixHeapLike {})
    }

    pub fn push(&mut self, value: f64, item: PyObject) -> PyResult<()> {
        match NotNan::new(value) {
            Ok(v) => {
                self.inner.push(-v, item);
                Ok(())
            }
            Err(_) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "value is NaN",
            )),
        }
    }

    pub fn pop(&mut self) -> PyResult<PyObject> {
        match self.inner.pop() {
            Some((_, item)) => Ok(item),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn pop_with_key(&mut self) -> PyResult<(f64, PyObject)> {
        match self.inner.pop() {
            Some((value, item)) => Ok((-value.into_inner(), item)),
            None => Err(PyErr::new::<pyo3::exceptions::PyIndexError, _>(
                "pop from empty heap",
            )),
        }
    }

    pub fn top(&self) -> Option<f64> {
        match self.inner.top() {
            Some(k) => Some(-k.into_inner()),
            None => None,
        }
    }

    pub fn clear(&mut self) {
        self.inner.clear();
    }

    pub fn __len__(&self) -> usize {
        self.inner.len()
    }
}
