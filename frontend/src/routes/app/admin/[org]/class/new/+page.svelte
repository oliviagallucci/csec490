<script lang="ts">
    import * as api from '$lib/api';
    import TextInput from '$lib/components/forms/TextInput.svelte';
    import Button from '$lib/components/generic/Button.svelte';

    export var classId: string;
    export var className: string;

    async function createClass() {
        var c:api.Class = {
            name: className,
            slug: classId,
            visible: false,
            uuid: crypto.randomUUID()
        }
        var res = await api.createClass(c);
        
    }
</script>

<TextInput label="Class Name" bind:value={className} id="class-name" autocomplete="off"/>
<TextInput label="Class ID" bind:value={classId} id="class-id" autocomplete="off"/>
<Button callback={()=>{createClass();}}>Create Class</Button>
