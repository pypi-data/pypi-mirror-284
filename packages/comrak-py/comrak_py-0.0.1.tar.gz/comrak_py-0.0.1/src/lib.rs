use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pymodule]
fn comrak_py(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(gfm_to_html, m)?)?;
    Ok(())
}

use comrak::{markdown_to_html, Options};

#[pyfunction]
fn gfm_to_html(md: &str) -> PyResult<String> {
    let mut options = Options::default();
    options.extension.strikethrough = true;
    options.extension.tagfilter = true;
    // options.render.unsafe_ = true;
    options.extension.table = true;
    options.extension.autolink = true;
    options.extension.tasklist = true;
    options.extension.footnotes = true;
    // options.extension.math_dollars = true;
    // options.extension.math_code = true;
    Ok(markdown_to_html(md, &options))
}
