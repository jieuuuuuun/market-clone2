const form = document.querySelector("#login-form");

const handleSubmit = async (event) => {
  event.preventDefault(); //리프레쉬방지
  const formData = new FormData(form);
  const sha256Password = sha256(formData.get("password"));
  formData.set("password", sha256Password);

  const res = await fetch("/login", {
    method: "post",
    body: formData,
  });
  const data = await res.json();
  const accessToken = data.access_token; //로컬스토리지에 저장해보자
  window.localStorage.setItem("token", accessToken);
  alert("로그인되었습니다.");

  window.location.pathname = "/";
};

form.addEventListener("submit", handleSubmit);
