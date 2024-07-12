#![allow(dead_code)]
use pyo3::prelude::*;

fn load_js_runtime(extensions: Vec<deno_core::Extension>) -> Result<deno_core::JsRuntime, deno_core::error::AnyError> {
    let js_runtime = deno_core::JsRuntime::try_new(deno_core::RuntimeOptions {
        module_loader: None,
        extensions: extensions,
        ..Default::default()
    })?;
    Ok(js_runtime)
}

#[pyfunction]
fn deno_js_runtime_for_python(codes: Vec<String>, eval_return: String) -> PyResult<String> {
    let extensions = vec![];
    let js_runtime_rs = load_js_runtime(extensions);
    if js_runtime_rs.is_err() {
        eprintln!("Failed to load js runtime");
    }
    let mut js_runtime = js_runtime_rs.unwrap();
    for code in codes {
        js_runtime.execute_script("eval_code", code).unwrap();
    }
    let eval_return = js_runtime.execute_script("eval_return", eval_return).unwrap();

    let scope = &mut js_runtime.handle_scope();
    let value = eval_return.open(scope);
    Ok(value.to_rust_string_lossy(scope))
}

#[pymodule]
fn js_runtime_for_python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(deno_js_runtime_for_python, m)?)?;
    Ok(())
}