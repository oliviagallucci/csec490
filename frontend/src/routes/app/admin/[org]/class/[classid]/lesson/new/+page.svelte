<script>
    import { page } from "$app/stores";
    import PortalNewLesson from "$lib/components/portals/PortalNewLesson.svelte";
    var classId = $page.params.classid;

</script>
<PortalNewLesson classId={classId}/>