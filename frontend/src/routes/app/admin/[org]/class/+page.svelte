<script>
    import SearchBox from "$lib/components/generic/SearchBox.svelte";
    var search = "";
</script>
<SearchBox bind:value={search} />
<p>{search}</p>