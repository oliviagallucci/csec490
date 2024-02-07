<script>
    import ContentStore from "$lib/components/contentStore/ContentStore.svelte";
    import Button from "$lib/components/generic/Button.svelte";

</script>
<div class="text-2xl font-header font-semibold">Lesson Store</div>
<div class="text-m font-light font-header">Showing <span class="font-semibold">12</span> lessons.</div>
<Button>Filter</Button>&nbsp;<Button>Add Repository</Button>
<br />
<br />

<ContentStore />