function toggleDetail(id) {
  const detail = document.getElementById("detail-" + id);
  if (detail.style.display === "none") {
    detail.style.display = "block";
  } else {
    detail.style.display = "none";
  }
}
