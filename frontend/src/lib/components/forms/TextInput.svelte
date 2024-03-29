<script>
    export var value = '';
    export var label = '';
    export var leading = ''
    export var id = '';
    export var autocomplete = '';
</script>

<div class="sm:col-span-4">
    <label for="username" class="block text-sm font-medium leading-6 text-gray-900">{label}</label>
    <div class="mt-2">
      <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
        {#if leading != ''}
        <span class="flex select-none items-center pl-3 text-gray-500 sm:text-sm">{leading}</span>
        {/if}
        <input type="text" name={label} id={id} autocomplete={autocomplete} bind:value={value} class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6">
      </div>
    </div>
  </div>