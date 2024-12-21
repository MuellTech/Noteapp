function deleteNote(noteId) {
  fetch("/remove-note", {
    method: "POST",  // Send a POST request to the server
    headers: {
      "Content-Type": "application/json", // Specify that the request body is JSON
    },
    body: JSON.stringify({ noteId: noteId }), // Convert the note ID to JSON and send it as the request body
  }).then((_res) => {
    window.location.href = "/"; // After the server responds, refresh the page by redirecting to the home page
  });
}

