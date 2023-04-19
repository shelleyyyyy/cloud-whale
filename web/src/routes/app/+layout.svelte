<script>
    import { goto } from "$app/navigation";
    import { pb } from "$lib/pocketbase.js"

    import logo from '$lib/cloudWhaleLogo.png'

    const logout = () => {
        pb.authStore.clear()

        goto('/login')
    }

</script>


<div class="navbar bg-base-100">
    <div class="flex-1">
        <img src={logo} alt="logo" class="w-20"/>
        <a class="btn btn-ghost normal-case text-xl" href="/app">Cloud Whale</a>
    </div>
    <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
            <li><a href="/app/machines">Machines</a></li>
            <li><a href="/app/create">Create</a></li>
            <button on:click={logout} class="btn">Logout</button>
        </ul>
    </div>
</div>

<slot/>