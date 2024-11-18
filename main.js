const inbox = document.getElementById("question");
document.getElementById('submit').addEventListener('click', async function() {
  const question = document.getElementById('question').value;
  // Simulated answer for demonstration purposes

  const data = await fetch('/get_answer/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'prompt': inbox.value
    }),
  }).then((response) => response.json())
    .catch((error) => console.error('Error:', error));
  
  console.log(data)
  document.getElementById('answer').value = data.response;
});