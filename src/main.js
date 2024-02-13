import App from "./App.svelte";
import "../firebase.json";

const app = new App({
  target: document.getElementById("app"),
});

export default app;
