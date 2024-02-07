<script>
    export let url = "";
    export let title = "";

</script>
<li>
    <a
        href={url}
        class="text-gray-400 hover:text-white hover:bg-gray-800 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold font-nav"
    >
    <span class="align-middle size-fit">
        <span class="align-middle">
            <slot name="icon">
            </slot>
        </span>
       
    </span>
        
        {title}
    </a>
</li>