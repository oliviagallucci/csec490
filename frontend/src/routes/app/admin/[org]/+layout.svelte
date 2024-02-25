<script>
    import OrgAdminSidebar from "$lib/components/sidebar/OrgAdminSidebar.svelte";
import SideBarPage from "$lib/components/sidebar/SideBarPage.svelte";

</script>
<SideBarPage title="Org">
    <OrgAdminSidebar slot="sidebar" />
    <slot></slot>
</SideBarPage>