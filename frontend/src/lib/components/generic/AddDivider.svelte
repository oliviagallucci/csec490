<script>
    import Button from "./Button.svelte";

    export var options = ["text","ctf","vm"];
    export var onAdd = (string)=>{};
    function callback(option){
        onAdd(option);
        open = false;
    }
    var open = false;
</script>
<br />
{#if open}
<div class="container mx-auto px-4 sm:p-6 lg:p-8  rounded transition-[height]">

<Button style="error" callback={()=>{open = false;}}>Close</Button>
<br />
<br />
<ul>
    {#each options as option}
    <Button callback={()=>{callback(option)}}>{option}</Button>&nbsp;
    {/each}
</ul>
</div>

{:else}
<div class="relative">
    <div class="absolute inset-0 flex items-center" aria-hidden="true">
      <div class="w-full border-t border-gray-300"></div>
    </div>
    <div class="relative flex justify-center">
      <span class="bg-white px-2 text-gray-500" on:click={()=>{open = !open;}}>
        <svg class="h-5 w-5 text-gray-500 hover:scale-150 transition" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z" />
        </svg>
      </span>
    </div>
  </div>
{/if}
  <br />
