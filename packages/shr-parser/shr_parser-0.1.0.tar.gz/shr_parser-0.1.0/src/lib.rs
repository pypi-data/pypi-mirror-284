use std::path::PathBuf;
use pyo3::prelude::*;
use ::shr_parser::{SHRParser, SHRParsingType};

#[pyfunction]
pub fn parse_file(file_path: String, parsing_type: i32) -> PyResult<String> {
    let path = PathBuf::from(file_path);
    let parsing_type = SHRParsingType::try_from(parsing_type)
        .map_err(|_| pyo3::exceptions::PyValueError::new_err("Invalid parsing type"))?;
    let parser = SHRParser::new(path, parsing_type)
        .map_err(|_| pyo3::exceptions::PyIOError::new_err("Failed to parse the file"))?;

    Ok(parser.to_str())
}

#[pymodule]
fn shr_parser(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_file, m)?)?;
    Ok(())
}
