<script>
    import Button from "$lib/components/generic/Button.svelte";
import PageTitle from "$lib/components/generic/PageTitle.svelte";
    import CtfCard from "$lib/components/renderable/CTFCard.svelte";
    import ProvisionCard from "$lib/components/renderable/ProvisionCard.svelte";
import TextCard from "$lib/components/renderable/TextCard.svelte";


</script>
<PageTitle>
  <span slot="title">Intro to Linux</span>
  <span slot="subtitle">Week 1</span>
  <span slot="actions"><Button callback={()=>{alert("Hello");}}>Save</Button></span>
</PageTitle>

<TextCard/>
<br />
<ProvisionCard />
<br />
<CtfCard/>