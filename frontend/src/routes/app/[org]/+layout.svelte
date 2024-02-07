<script>
    import LearnSidebar from "$lib/components/sidebar/LearnSidebar.svelte";
import SideBarPage from "$lib/components/sidebar/SideBarPage.svelte";
import { page } from '$app/stores';
var orgName = $page.params.org;
</script>
<SideBarPage title={orgName}>
    <LearnSidebar slot="sidebar"/>
    <slot></slot>
</SideBarPage>