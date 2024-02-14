<script>
  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import Router from 'svelte-spa-router';
  import './css/style.css';
  import {user$} from './store';
  import {
    getAuth, 
    GoogleAuthProvider, 
    signInWithCredential
  } from "firebase/auth"
  import { onMount } from "svelte";
  import Loading from "./pages/Loading.svelte";
  import MyPage from "./pages/MyPage.svelte";
  
  //로그인 유지하기 위한 코드 수정 1. 처음에는 true로 해준다 처음에 딱 
  //화면이 갔을 때는 로딩화면을 보여준다. 42~49줄 
  let isLoading = true;

  const auth = getAuth()

  const checkLogin = async () => {
    const token = localStorage.getItem("token");
    //여기있는 토큰이 없어서 그냥 리턴될 때 isLoading이 false가 되어야 한다. 
    if (!token) return (isLoading = false);

    const credential = GoogleAuthProvider.credential(null, token);  //액세스토큰이다.
    const result = await signInWithCredential(auth, credential);
    const user = result.user;
    user$.set(user)
    //그리고 여기서 유저를 가져와서 데이터를 업데이트해서 성공했을 때 isLoading이 false가 되어야한다. 
    isLoading = false
  }

 const routes = {
  '/':Main,
  '/signup':Signup,
  '/write':Write,
  "/my":MyPage,
  "*":NotFound
 };
// onMount를 사용하여 화면이 렌더링 될 때마다 checkLogin을 실행한다. 
 onMount(() => checkLogin())
</script>
<!-- 2. isLoading 이면 로딩 화면을 보여준다.  -->
{#if isLoading}
  <Loading />
<!-- writable 값을 가져오려면 $를 붙여서 가져와야한다.  -->
{:else if !$user$}
  <Login/>
{:else}
  <Router {routes} />
{/if}

