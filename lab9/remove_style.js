function remove_style() {
    document.getElementsByTagName("LINK")[0].removeAttribute("href");
}

function set_style() {
    document.getElementsByTagName("LINK")[0].setAttribute("href", "sheet.css");
}