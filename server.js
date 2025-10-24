import express from "express";
const app = express();

app.use(express.static("public"));

// Rewrite rule: /about → /about.html
app.get("/:page", (req, res) => {
  res.sendFile(`${process.cwd()}/public/${req.params.page}.html`);
});

app.listen(3000, () => console.log("Server running at http://localhost:3000"));