import { getClasses } from "$lib/api";


export async function load() {
    return {
        class: await getClasses()
    };
}