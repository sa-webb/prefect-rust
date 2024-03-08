use pyo3::{exceptions::PyValueError, prelude::*};

#[pyfunction]
fn sum(a: usize, b: usize) -> PyResult<usize> {
    Ok(a + b)
}

#[pyfunction]
fn extract_city_state(location: &str) -> PyResult<(String, String)> {
    let parts: Vec<&str> = location.split(',').collect();
    if parts.len() != 2 {
        return Err(PyValueError::new_err("Invalid location format"));
    }
    Ok((parts[0].trim().to_string(), parts[1].trim().to_string()))
}

#[pymodule]
fn pyrust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum, m)?)?;
    m.add_function(wrap_pyfunction!(extract_city_state, m)?)?;
    Ok(())
}
