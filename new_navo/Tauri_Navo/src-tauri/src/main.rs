// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
use tauri::Manager;
// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
async fn open_settings_window(app: tauri::AppHandle) {
    let window = app.get_window("home").unwrap();
    window.hide().unwrap();

}


fn main() {
    tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![
        open_settings_window,
        
    ])
.run(tauri::generate_context!())
.expect("error while running tauri application");

}
