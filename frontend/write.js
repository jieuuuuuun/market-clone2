const form = document.getElementById("write-form");

const hadleSubmitForm = async (event) => {
  event.preventDefault();
  const body = new FormData(form);
  //세계시간 기준으로
  body.append("insertAt", new Date().getTime());
  try {
    const res = await fetch("/items", {
      method: "post",
      body: body,
    });
    const data = await res.json();
    if (data === "200") window.location.pathname = "/";
    else console.error("이미지 업로드에 실패했습니다.");
  } catch (e) {
    console.error(e);
  }
};

form.addEventListener("submit", hadleSubmitForm);
