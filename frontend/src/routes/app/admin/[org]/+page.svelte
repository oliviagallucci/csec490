<script>
    import Button from "$lib/components/generic/Button.svelte";
import PageTitle from "$lib/components/generic/PageTitle.svelte";

</script>

<PageTitle>
    <span slot="title">Hello, <span class="font-semibold">John Smith</span></span>
    <span slot="subtitle">Your next event is in 2 days.</span>
    <span slot="actions"><Button callback={()=>{alert("Hello");}}>New Lesson</Button>&nbsp;<Button style="secondary">New Class</Button></span>
  </PageTitle>