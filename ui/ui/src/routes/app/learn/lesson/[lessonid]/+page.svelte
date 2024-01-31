<script>
    import CtfCard from "$lib/components/renderable/CTFCard.svelte";
    import ProvisionCard from "$lib/components/renderable/ProvisionCard.svelte";
import TextCard from "$lib/components/renderable/TextCard.svelte";


</script>
<div class="md:flex md:items-center md:justify-between mb-10">
    <div class="min-w-0 flex-1">
      <h2 class="text-2xl font-header leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">Intro to Linux</h2>
    </div>
    <div class="mt-4 flex md:ml-4 md:mt-0">
      <button type="button" class="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">Edit</button>
      <button type="button" class="ml-3 inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Publish</button>
    </div>
  </div>

<TextCard />
<br />
<ProvisionCard />
<br />
<CtfCard />