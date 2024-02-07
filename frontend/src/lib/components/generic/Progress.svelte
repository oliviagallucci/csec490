<script>
    export let value = 0;
</script>
<div class="flex-start flex h-2.5 w-full overflow-hidden rounded-full bg-blue-gray-50 font-sans text-xs font-medium">
    <div class="flex h-full items-center justify-center overflow-hidden break-all rounded-full bg-gray-900 text-white transition-all" style:width={`${value}%`}></div>
  </div>