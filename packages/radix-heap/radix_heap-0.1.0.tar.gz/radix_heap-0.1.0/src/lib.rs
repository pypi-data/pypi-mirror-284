use pyo3::prelude::*;
mod pylib;

#[pymodule]
fn radix_heap(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<pylib::PyRadixMaxHeapInt>()?;
    m.add_class::<pylib::PyRadixMinHeapInt>()?;
    m.add_class::<pylib::PyRadixMaxHeap>()?;
    m.add_class::<pylib::PyRadixMinHeap>()?;
    Ok(())
}
