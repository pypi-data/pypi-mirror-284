<svelte:options accessors={true} />

<script lang="ts">
    import type { Gradio } from "@gradio/utils";
    import type { LoadingStatus } from "@gradio/statustracker";
    import { tick } from "svelte";
    import {
        Table,
        TableBody,
        TableBodyCell,
        TableBodyRow,
        TableHead,
        TableHeadCell,
        Input,
        Toggle,
        Textarea,
        Select,
        Tooltip,
    } from "flowbite-svelte";

    export let gradio: Gradio<{
        change: never;
        submit: never;
        input: never;
        clear_status: LoadingStatus;
    }>;
    export let value;
    export let max_height;
    export let params: {
        name: string;
        description: string;
        defaultValue: any;
        value: any;
        type: "string" | "number" | "boolean" | "dict" | "list" | "enum";
        options?: any;
    }[];
    window.process = {
        env: {
            NODE_ENV: "production",
            LANG: "",
        },
    };

    let el: HTMLTextAreaElement | HTMLInputElement;
    const container = true;

    function handle_change(): void {
        gradio.dispatch("change");
    }

    async function handle_keypress(e: KeyboardEvent): Promise<void> {
        await tick();
        if (e.key === "Enter") {
            e.preventDefault();
            gradio.dispatch("submit");
        }
    }

    // When the value changes, dispatch the change event via handle_change()
    // See the docs for an explanation: https://svelte.dev/docs/svelte-components#script-3-$-marks-a-statement-as-reactive
    $: value, handle_change();

    $: max_height;

    let editParams = params;
    const updateEditParams = () => {
        if (!params?.length) return;
        editParams = params.map((item) => {
            if (item.type === "dict" || item.type === "list") {
                return {
                    ...item,
                    defaultValue: JSON.stringify(item.defaultValue),
                    value: JSON.stringify(item.value),
                };
            }
            return item;
        });
    };

    $: params, updateEditParams();

    const update = () => {
        const res = editParams.map((item) => {
            if (item.type === "dict" || item.type === "list") {
                return {
                    ...item,
                    defaultValue: JSON.parse(item.defaultValue),
                    value: JSON.parse(item.value),
                };
            }
            if (item.type === "number") {
                return {
                    ...item,
                    value: +item.value,
                };
            }
            return item;
        });
        console.log(res);
        value = JSON.stringify(res);
        params = res;
    };

    let tableWidth = 0;
    $: tableWidth;
    const interval = setInterval(() => {
        if (document.getElementById("storybook-table")) {
            const observer = new ResizeObserver((entries) => {
                tableWidth = entries[0].contentRect.width;
            });
            observer.observe(document.getElementById("storybook-table"));
            clearInterval(interval);
        }
    }, 1000);
</script>

<div
    style={max_height !== undefined ? `max-height: ${max_height}px;` : ""}
    id="storybook-table"
>
    {#if !params?.length}
        <div style="width: 100%; height: 240px;display: flex;align-items: center;justify-content: center;border: 1px solid #4b5563;">
            <h1>No parameter</h1>
        </div>
    {/if}
    {#if params?.length}
    <Table hoverable={true}>
        <TableHead>
            <TableHeadCell>
                <div style="width: 100px; text-align: start;">Name</div>
            </TableHeadCell>
            <TableHeadCell>
                <div style="width: 180px; text-align: start;">Description</div>
            </TableHeadCell>
            <TableHeadCell>
                <div
                    style="width: {(tableWidth - 280) / 2}px; text-align: start;"
                >
                    Default
                </div>
            </TableHeadCell>
            <TableHeadCell>
                <div
                    style="width: {(tableWidth - 280) / 2}px; text-align: start;"
                >
                    Control
                </div>
            </TableHeadCell>
        </TableHead>
        <TableBody tableBodyClass="divide-y">
            {#each editParams as param}
                <TableBodyRow>
                    <TableBodyCell>
                        <div style="width: 100px" class="ellipsis-single-line">
                            <span>{param.name}</span>
                            <Tooltip type="light">{param.name}</Tooltip>
                        </div>
                    </TableBodyCell>
                    <TableBodyCell>
                        <div style="width: 180px;overflow-wrap: break-word;">
                            <div>{param.description}</div>
                        </div>
                    </TableBodyCell>
                    <TableBodyCell>
                        <div style="width: {(tableWidth - 280) / 2}px">
                            <span>{param.defaultValue}</span>
                        </div>
                    </TableBodyCell>
                    <TableBodyCell>
                        <div
                            style="width: {(tableWidth - 280) / 2}px"
                            class="storybook-input"
                        >
                            {#if param.type === "string" || param.type === "dict" || param.type === "list"}
                                <Textarea
                                    bind:value={param.value}
                                    on:change={update}
                                    style="background-color: rgb(17 24 39);"
                                />
                            {/if}
                            {#if param.type === "number"}
                                <Input
                                    type="number"
                                    bind:value={param.value}
                                    on:change={update}
                                    style="background-color: rgb(17 24 39);"
                                />
                            {/if}
                            {#if param.type === "boolean"}
                                <Toggle
                                    bind:checked={param.value}
                                    on:change={update}
                                    style="background-color: rgb(17 24 39);"
                                />
                            {/if}
                            {#if param.type === "enum"}
                                <Select
                                    bind:value={param.value}
                                    on:change={update}
                                    items={param.options.map((item) =>
                                        Array.isArray(item)
                                            ? { value: item[0], name: item[1] }
                                            : { value: item, name: item },
                                    )}
                                    style="background-color: rgb(17 24 39);"
                                />
                            {/if}
                        </div>
                    </TableBodyCell>
                </TableBodyRow>
            {/each}
        </TableBody>
    </Table>
    {/if}
</div>

<style>
    .ellipsis-single-line {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 200px;
        display: block;
    }
</style>
