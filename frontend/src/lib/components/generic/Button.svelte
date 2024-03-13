<script>
    export let callback = () => {};
    /**
     * Specify the style of the button
     * @property style {('primary'|'secondary'|'ok'|'warn'|'error')}
     */
    export let style="primary";
</script>
<style>
    .primary{
        @apply bg-orange-600 text-white hover:bg-orange-500 focus-visible:outline-orange-600;
    }
    .secondary{
        @apply bg-gray-300 text-black hover:bg-gray-400 focus-visible:outline-black;
    }
    .ok{
        @apply bg-green-600 text-white hover:bg-green-500 focus-visible:outline-green-600;
    }
    .warn{
        @apply bg-yellow-400 text-black hover:bg-yellow-500 focus-visible:outline-yellow-600;

    }
    .error{
        @apply bg-red-600 text-white hover:bg-red-500 focus-visible:outline-red-600;

    }
</style>
<button type="button" class="rounded-md px-3 py-2 text-sm font-semibold shadow-sm  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 {style} transition" on:click={callback}><slot></slot></button>
