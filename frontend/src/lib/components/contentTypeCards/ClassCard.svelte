<script lang="ts">
    import * as api from '$lib/api';
    export var c: api.Class = {};

   
</script>

<div class="w-full h-full rounded-2xl shadow-2xl overflow-hidden">
    <img src="/graphics/ClassPlaceholder.svg" alt="Class Placeholder" />
    <div class="p-8">
        <h1 class="font-header text-lg md:text-xl lg:text-2xl">{c.name}</h1>
        <div class="py-4">
            <slot name="actions"></slot>
        </div>
        

    </div>
</div>