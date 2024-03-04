<script>
    var step = 0;
    export var source = "";

    /**
     * Callback for a source select
     * @param s {string} The source that was selected
     */
    function onSelectSource(s){
        source = s;
        step = 1;
    }

</script>

{#if step == 0}
    <h2 class="text-2xl text-center">Create a Lesson</h2>
    <div class="container mx-auto px-4 sm:p-6 lg:p-8  rounded transition-[height]">
        <div class="mt-6 grid grid-cols-1 gap-y-10 sm:grid-cols-2 sm:gap-x-6 sm:gap-y-0 lg:gap-x-8 justify-between align-items-center">
            <div class="group relative w-fit mx-auto">
                <button class="relative mx-auto" on:click={()=>{onSelectSource("store")}}>
                    <div class="h-96 w-full overflow-hidden rounded-lg aspect-1 group-hover:opacity-75 sm:h-auto">
                        <img src="/icons/cart.svg" class="w-full h-full" alt="shopping cart">
                      </div>
                      <h3 class="mt-4 text-base font-semibold text-gray-900 text-2xl text-center">
                        From Content Store
                      </h3>
                </button>
             
            </div>
            <div class="group relative w-fit mx-auto">
                <button class="relative mx-auto" on:click={()=>{onSelectSource("new")}}>
                    <div class="h-96 w-full overflow-hidden rounded-lg aspect-1 group-hover:opacity-75 sm:h-auto">
                        <img src="/icons/add.svg" class="w-full h-full" alt="add button">
                      </div>
                      <h3 class="mt-4 text-base font-semibold text-gray-900 text-2xl text-center">
                        Start New
                      </h3>
                </button>
             
            </div>
           </div>
    </div>
{/if}