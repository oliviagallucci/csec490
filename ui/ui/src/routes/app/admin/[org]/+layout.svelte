<script>
import SideBarPage from "$lib/components/sidebar/SideBarPage.svelte";
import { page } from '$app/stores';
    import OrgAdminSidebar from "$lib/components/sidebar/OrgAdminSidebar.svelte";
var orgName = $page.params.org;
</script>
<SideBarPage title={orgName}>
    <OrgAdminSidebar slot="sidebar"/>
    <slot></slot>
</SideBarPage>