const form = document.getElementById("postForm");
const postsDiv = document.getElementById("posts");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(form);

  const res = await fetch("http://localhost:5000/posts", {
    method: "POST",
    body: formData,
  });

  const post = await res.json();
  addPostToDOM(post);
  form.reset();
});

async function loadPosts() {
  const res = await fetch("http://localhost:5000/posts");
  const posts = await res.json();
  postsDiv.innerHTML = "";
  posts.forEach(addPostToDOM);
}

function addPostToDOM(post) {
  const div = document.createElement("div");
  div.innerHTML = `<h2>${post.title}</h2><p>${post.content}</p>${
    post.image ? `<img src="http://localhost:5000${post.image}" />` : ""
  }`;
  postsDiv.prepend(div);
}

loadPosts();
