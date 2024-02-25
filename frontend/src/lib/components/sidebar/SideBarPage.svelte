<script>
    import { fade, slide } from "svelte/transition";
    let offCanvasOpen = false;
    export let title = "";
</script>

<div>
    <!-- Off-canvas menu for mobile, show/hide based on off-canvas menu state. -->
    <div class="relative z-50 lg:hidden" role="dialog" aria-modal="true">
        <!--
        Off-canvas menu backdrop, show/hide based on off-canvas menu state.
  
        Entering: "transition-opacity ease-linear duration-300"
          From: "opacity-0"
          To: "opacity-100"
        Leaving: "transition-opacity ease-linear duration-300"
          From: "opacity-100"
          To: "opacity-0"
      -->
        {#if offCanvasOpen}
            <div
                transition:fade={{ duration: 300 }}
                class="fixed inset-0 bg-gray-900/80"
                on:click={() => {
                    offCanvasOpen = false;
                }}
                aria-label="Close off-canvas menu"
            ></div>
        {/if}
            <div
                class="fixed inset-0 flex transform ease-in-out duration-300 transform {offCanvasOpen ? '-translate-x-0' : '-translate-x-full'}"

                transition:slide={{ duration: 300, axis: "x" }}
            >
                <!--
          Off-canvas menu, show/hide based on off-canvas menu state.
  
          Entering: "transition ease-in-out duration-300 transform"
            From: "-translate-x-full"
            To: "translate-x-0"
          Leaving: "transition ease-in-out duration-300 transform"
            From: "translate-x-0"
            To: "-translate-x-full"
        -->

                <div
                    transition:slide={{ duration: 300, axis: "x" }}
                    class="relative mr-16 flex w-full max-w-xs flex-1"
                >
                    <!--
            Close button, show/hide based on off-canvas menu state.
  
            Entering: "ease-in-out duration-300"
              From: "opacity-0"
              To: "opacity-100"
            Leaving: "ease-in-out duration-300"
              From: "opacity-100"
              To: "opacity-0"
          -->
                    <div
                        class="absolute left-full top-0 flex w-16 justify-center pt-5"
                        transition:fade={{ duration: 300 }}
                    >
                        <button
                            type="button"
                            class="-m-2.5 p-2.5"
                            on:click={() => {
                                offCanvasOpen = false;
                            }}
                        >
                            <span class="sr-only">Close sidebar</span>
                            <svg
                                class="h-6 w-6 text-white"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke-width="1.5"
                                stroke="currentColor"
                                aria-hidden="true"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    d="M6 18L18 6M6 6l12 12"
                                />
                            </svg>
                        </button>
                    </div>

                    <!-- Sidebar component, swap this element with another sidebar if you like -->
                    <slot name="sidebar">
                        </slot>
                </div>
            </div>
    </div>

    <!-- Static sidebar for desktop -->
    <div
        class="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col"
    >
        <slot name="sidebar"></slot>
        
    </div>

    <div
        class="sticky top-0 z-40 flex items-center gap-x-6 bg-gray-900 px-4 py-4 shadow-sm sm:px-6 lg:hidden"
    >
        <button
            type="button"
            class="-m-2.5 p-2.5 text-gray-400 lg:hidden"
            on:click={() => {
                offCanvasOpen = true;
            }}
        >
            <span class="sr-only">Open sidebar</span>
            <svg
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
                />
            </svg>
        </button>
        <div class="flex-1 text-sm font-semibold leading-6 text-white">
            {title}
        </div>
        <a href="#">
            <span class="sr-only">Your profile</span>
            <img
                class="h-8 w-8 rounded-full bg-gray-800"
                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                alt=""
            />
        </a>
    </div>

    <main class="py-10 lg:pl-72">
        <div class="px-4 sm:px-6 lg:px-8">
            <!-- Your content -->
            <slot />
        </div>
    </main>
</div>
