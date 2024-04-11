<script>
    import ContentStore from "$lib/components/contentStore/ContentStore.svelte";
    import Button from "$lib/components/generic/Button.svelte";
    import PageTitle from "$lib/components/generic/PageTitle.svelte";
    import SearchBox from "$lib/components/generic/SearchBox.svelte";
    var search = "";

</script>
<PageTitle>
    <span slot="title">Lesson Store</span>
</PageTitle>
<SearchBox bind:value={search} />
<div class="mx-auto mt-10 max-w-7xl px-6 lg:px-8">


<ContentStore />
</div>