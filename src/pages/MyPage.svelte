<script>
    import Nav from "../components/Nav.svelte";
  import { user$ } from "../store";
//로그아웃은 유저정보를 비워주고 로컬스토리지를 비워준다. 
    const logout = () => {
        user$.set(null)
        localStorage.removeItem("token")
    }
</script>

<div>나의 당근</div>
<button on:click={logout}>로그아웃</button>
<Nav location="my"/>

<style>
    button {
        cursor: pointer;
        border:1px solid rgba(0, 0, 0, 0.3)
    }
</style>