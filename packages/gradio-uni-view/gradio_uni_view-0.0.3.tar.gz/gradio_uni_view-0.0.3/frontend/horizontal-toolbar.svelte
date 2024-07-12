<svelte:options accessors={true} />

<script lang="ts">
    import Checkbox from '@smui/checkbox';
    import Textfield from '@smui/textfield';
    import type { Gradio } from "@gradio/utils";
    import { Block } from "@gradio/atoms";
    import type { LoadingStatus } from "@gradio/statustracker";
    import { tick } from "svelte";
    import {
        Granularity,
        LightPlugin,
        Color,
        RepresentationType,
        AtomReprType,
        MolecularReprType,
        HierarchyType,
        queryCellItemsByHierarchyType,
    } from "dpmol";
    import { KRadio } from '@ikun-ui/radio';
	import { KRadioGroup } from '@ikun-ui/radio-group';
    import { KDropdown, KDropdownItem } from "@ikun-ui/dropdown";
	import './index.css';
	import './index.less';
    
    enum ExpandFilter {
        All = 0,
        Residues,
        Water,
        SolventWithoutWater,
        Solvent
    }
    const ToolbarWidth = 698;
    export let gradio: Gradio<{
        change: never;
        submit: never;
        input: never;
        clear_status: LoadingStatus;
    }>;
    export let lightPlugin;
    export let isFixedRight;
    export let rootWidth;
    export let selectionHistory;

    let style = "";
    const updateStyle = () => {
        style = `width: ${expanded ? rootWidth : 46}px; overflowX: ${isFixedRight ? "scroll" : "hidden"}`;
    };
    $: isFixedRight, updateStyle();
    $: rootWidth, updateStyle();
    let expanded = true;

    let pickModeVisible = false;
    $: pickModeVisible;

    let currGranularity = Granularity.Residue;
    const pickLevelText = (currGranularity) => {
        if (currGranularity === Granularity.Atom) return "Atom";
        if (currGranularity === Granularity.Residue) return "Residue";
        if (currGranularity === Granularity.Chain) return "Chain";
        if (currGranularity === Granularity.Molecular) return "Molecule";
        return "Residue";
    };
    const quickSelect = (type: HierarchyType) => {
        const func = () => {
            lightPlugin.managers.selection.structure.clear();
            const queryData = queryCellItemsByHierarchyType(lightPlugin);
            Object.keys(queryData).forEach((ref) => {
                const item = queryData[ref];
                const data =
                    type === HierarchyType.Solvent
                        ? [...item[type], ...item[HierarchyType.Water]]
                        : item[type];
                if (data.length) {
                    lightPlugin.managers.selection.structure.add(
                        {
                            item: {
                                ref,
                                elementIds:
                                    (data
                                        .map((item) => item.elementIds)
                                        .flat() as number[]) ?? [],
                            },
                        },
                        false,
                    );
                }
            });
        };
        func();
    };

	let surroundingDropdownRef: any = null;
    let surroundingVisible = false;
    $: surroundingVisible;
    let surroundingRadius = 3;
    $: surroundingRadius;
    let expandFilter = ExpandFilter.All
    $: expandFilter;
    let asWholeResidueState = 1;
    $: asWholeResidueState;
    let excludeSelectedAtoms = false;
    $: excludeSelectedAtoms;
</script>

<div class="uni-view-horizontal-toolbar-container">
    <div {style} class="uni-view-horizontal-toolbar-inner row">
        <!-- Quick Select -->
        <div style="margin: 4px 8px;">
            <div
                class="uni-view-horizontal-toolbar-title row"
                style={`width: ${expanded ? ToolbarWidth : 46}`}
            >
                Quick Select
            </div>
            <div class="row">
                <div
                    class="uni-view-horizontal-toolbar-item"
                    style={expanded ? "" : `position: relative;top: -8px;`}
                >
                    <KDropdown
                        on:change={(e) => {
                            pickModeVisible = e.detail;
                        }}
                        on:command={(e) => {
                            currGranularity = e.detail;
                            lightPlugin.managers.selection.structure.setGranularity(
                                e.detail,
                            );
                        }}
                        trigger="click"
                    >
                        <div
                            class="row"
                            style={"flex-shrink: 0; align-items: center; justify-content: center;"}
                        >
                            <!-- <Wrapper> -->
                            <div>
                                {#if currGranularity === Granularity.Atom}
                                    <svg
                                        width="1em"
                                        height="1em"
                                        viewBox="0 0 20 20"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                        class="normal-icon"
                                    >
                                        <path
                                            d="M20 0H0v20h20V0z"
                                            fill="#fff"
                                            fill-opacity=".01"
                                        />
                                        <circle
                                            cx="10"
                                            cy="10"
                                            r="1.25"
                                            fill="#A2A5C4"
                                        />
                                        <path
                                            d="M16.908 3.062c1.569 1.569-.26 5.94-4.083 9.763-3.823 3.824-8.194 5.652-9.763 4.083-1.569-1.569.26-5.94 4.083-9.763 3.823-3.824 8.194-5.652 9.763-4.083z"
                                            stroke="#A2A5C4"
                                            stroke-width="1.3"
                                            stroke-linecap="square"
                                            stroke-linejoin="round"
                                        />
                                        <path
                                            d="M3.117 3.062c-1.569 1.569.259 5.94 4.082 9.763 3.824 3.824 8.195 5.652 9.764 4.083 1.568-1.569-.26-5.94-4.083-9.763C9.056 3.32 4.685 1.493 3.117 3.062z"
                                            stroke="#A2A5C4"
                                            stroke-width="1.3"
                                            stroke-linecap="square"
                                            stroke-linejoin="round"
                                        />
                                    </svg>
                                {/if}
                                {#if currGranularity === Granularity.Residue}
                                    <svg
                                        class="normal-icon"
                                        width="1em"
                                        height="1em"
                                        viewBox="0 0 20 20"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                    >
                                        <path
                                            d="M17.071 5.596l-6.666-3.704a.833.833 0 0 0-.81 0L2.93 5.596a.833.833 0 0 0-.429.728v7.353c0 .302.164.581.429.728l6.666 3.704c.252.14.558.14.81 0l6.666-3.704M5.5 12.5L10 15"
                                            stroke="#A2A5C4"
                                            stroke-width="1.3"
                                            stroke-linecap="round"
                                        />
                                        <path
                                            stroke="#A2A5C4"
                                            stroke-linecap="round"
                                            stroke-dasharray="1 2"
                                            d="M17.5 7.5v5"
                                        />
                                    </svg>
                                {/if}
                                {#if currGranularity === Granularity.Chain}
                                    <svg
                                        class="normal-icon"
                                        width="1em"
                                        height="1em"
                                        viewBox="0 0 20 20"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                    >
                                        <path
                                            d="M12.9141 8.75032L14.5807 7.50033L18.3307 10.0003V14.167L14.1641 16.667L9.99739 14.167V5.41699L5.41406 2.91699L1.66406 5.41699V10.0003L5.41406 12.5003L7.08073 11.2503"
                                            stroke="#A2A5C4"
                                            stroke-width="1.3"
                                            stroke-linecap="square"
                                            stroke-linejoin="round"
                                        />
                                    </svg>
                                {/if}
                                {#if currGranularity === Granularity.Molecular}
                                    <svg
                                        class="normal-icon"
                                        width="1em"
                                        height="1em"
                                        viewBox="0 0 20 20"
                                        fill="none"
                                        xmlns="http://www.w3.org/2000/svg"
                                    >
                                        <path
                                            d="M20 0H0V20H20V0Z"
                                            fill="white"
                                            fill-opacity="0.01"
                                        />
                                        <path
                                            d="M17.9167 14.9993C17.9167 15.5583 17.6965 16.0659 17.3382 16.4401C16.959 16.8361 16.425 17.0827 15.8333 17.0827C14.6827 17.0827 13.75 16.1499 13.75 14.9993C13.75 14.1618 14.2442 13.4397 14.957 13.1088C15.2233 12.9851 15.5203 12.916 15.8333 12.916C16.9839 12.916 17.9167 13.8488 17.9167 14.9993Z"
                                            stroke="#A2A5C4"
                                            stroke-width="1.25"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                        />
                                        <path
                                            d="M6.2526 14.9993C6.2526 15.5583 6.03244 16.0659 5.67415 16.4401C5.2949 16.8361 4.7609 17.0827 4.16927 17.0827C3.01868 17.0827 2.08594 16.1499 2.08594 14.9993C2.08594 14.1618 2.58016 13.4397 3.29288 13.1088C3.55929 12.9851 3.85622 12.916 4.16927 12.916C5.31985 12.916 6.2526 13.8488 6.2526 14.9993Z"
                                            stroke="#A2A5C4"
                                            stroke-width="1.25"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                        />
                                        <path
                                            d="M12.0807 3.74935C12.0807 4.30835 11.8606 4.81589 11.5023 5.19006C11.123 5.5861 10.589 5.83268 9.9974 5.83268C8.84681 5.83268 7.91406 4.89993 7.91406 3.74935C7.91406 2.91181 8.40827 2.18971 9.12102 1.85877C9.3874 1.73507 9.68435 1.66602 9.9974 1.66602C11.148 1.66602 12.0807 2.59876 12.0807 3.74935Z"
                                            stroke="#A2A5C4"
                                            stroke-width="1.25"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                        />
                                        <path
                                            d="M9.99996 11V6M9.99996 11L5.625 13.5259L9.99996 11ZM9.99996 11L14.3749 13.5259L9.99996 11Z"
                                            stroke="#A2A5C4"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            stroke-dasharray="2 2"
                                        />
                                        <path
                                            d="M9 5.5L4 13M11 5.5L16 13"
                                            stroke="#A2A5C4"
                                            stroke-linejoin="round"
                                        />
                                        <path
                                            d="M6 15L14 15"
                                            stroke="#A2A5C4"
                                            stroke-linejoin="round"
                                        />
                                    </svg>
                                {/if}
                            </div>
                            <!-- <Tooltip>
                                    {`Pick ${pickLevelText(currGranularity)}`}
                                </Tooltip> -->
                            <!-- </Wrapper> -->
                            <svg
                                width="1em"
                                height="1em"
                                viewBox="0 0 8 8"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                                style={`
                                    transform: ${pickModeVisible ? "rotate(0)" : "rotate(180deg)"};
                                    font-size: 8px;
                                    color: #a2a5ca;
                                `}
                            >
                                <path
                                    d="M6.95641 5.66979L4.15766 2.07713C4.07755 1.97429 3.9233 1.97429 3.84234 2.07713L1.04359 5.66979C0.939613 5.80376 1.03336 6 1.20125 6L6.79875 6C6.96664 6 7.06039 5.80376 6.95641 5.66979Z"
                                    fill="#888BAB"
                                />
                            </svg>
                        </div>
                        <div slot="dropdown" class="menu-normal">
                            <KDropdownItem command={Granularity.Atom}>
                                <div class="row" style={"align-items: center"}>
                                    <!-- <AtomIcon className={styles['normal-icon']} /> -->
                                    Atom
                                </div>
                            </KDropdownItem>
                            <KDropdownItem command={Granularity.Residue}>
                                <div class="row" style={"align-items: center"}>
                                    <!-- <ResidueIcon className={styles['normal-icon']} /> -->
                                    Residue
                                </div>
                            </KDropdownItem>
                            <KDropdownItem command={Granularity.Chain}>
                                <div class="row" style={"align-items: center"}>
                                    <!-- <ChainIcon className={styles['normal-icon']} /> -->
                                    Chain
                                </div>
                            </KDropdownItem>
                            <KDropdownItem command={Granularity.Molecular}>
                                <div class="row" style={"align-items: center"}>
                                    <!-- <MolecularIcon className={styles['normal-icon']} /> -->
                                    Molecule
                                </div>
                            </KDropdownItem>
                        </div>
                    </KDropdown>
                    <div class={"uni-view-horizontal-toolbar-subtitle"}>
                        {pickLevelText(currGranularity)}
                    </div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <svg
                        on:click={() => quickSelect(HierarchyType.Protein)}
                        style="margin-left: 5"
                        class="uni-view-horizontal-toolbar-icon uni-view-horizontal-toolbar-dropdown"
                        xmlns="http://www.w3.org/2000/svg"
                        width="1em"
                        height="1em"
                        fill="none"
                        viewBox="0 0 20 20"
                    >
                        <path
                            fill="#A2A5C4"
                            d="M10.61 8.936a.6.6 0 0 1 .6-.6h3.543c2.38 0 3.57 1.008 3.57 3.038 0 2.044-1.204 3.066-3.598 3.066h-2.59v3.292a.6.6 0 0 1-.6.6h-.326a.6.6 0 0 1-.6-.6V8.936Zm1.525.702v3.5h2.492c.756 0 1.302-.14 1.652-.42.336-.28.518-.728.518-1.344 0-.616-.182-1.064-.532-1.316-.35-.28-.896-.42-1.638-.42h-2.492Z"
                        />
                        <path
                            stroke="#A2A5C4"
                            stroke-linecap="round"
                            stroke-width="1.3"
                            d="m9.607 7.14-.283-.826s-.118-1.327.699-2.564 2.184-1.61 2.184-1.61l1.892 4.174"
                        />
                        <path
                            stroke="#A2A5C4"
                            stroke-width="1.3"
                            d="M3.738 8.955C4.556 7.718 5.61 7.32 5.61 7.32l2.053 4.927s.362 1.252-.291 2.241c-.653.99-1.86 2.097-2.05 2.207l-2.188-5.714s-.213-.79.604-2.027Z"
                        />
                        <path
                            stroke="#A2A5C4"
                            stroke-linecap="round"
                            stroke-width="1.3"
                            d="M9.472 7.146 8.77 6.99s-1.9-.575-3.512.463c-1.181.76-1.812 2.398-1.912 2.64l3.064.786 1.531.393.766.196"
                        />
                    </svg>
                    <!-- <Tooltip trigger={['hover', 'click']} title="Select Proteins" placement="bottom"> -->
                    <!-- </Tooltip> -->
                    <div class="uni-view-horizontal-toolbar-subtitle">
                        Protein
                    </div>
                </div>

                <div class="uni-view-horizontal-toolbar-item">
                    <svg
                        on:click={() => quickSelect(HierarchyType.Ligand)}
                        style="margin-left: 5"
                        class="uni-view-horizontal-toolbar-icon uni-view-horizontal-toolbar-dropdown"
                        xmlns="http://www.w3.org/2000/svg"
                        width="1em"
                        height="1em"
                        fill="none"
                        viewBox="0 0 20 20"
                    >
                        <path
                            stroke="#A2A5C4"
                            stroke-linecap="round"
                            d="M1.664 8.858h1.273"
                        />
                        <path
                            stroke="#A2A5C4"
                            stroke-width="1.3"
                            d="m3.011 8.697 1.616-2.654a.37.37 0 0 1 .318-.17h3.208a.37.37 0 0 1 .318.17l1.616 2.654c.061.1.061.222 0 .323l-1.616 2.654a.37.37 0 0 1-.318.17H4.945a.37.37 0 0 1-.318-.17L3.011 9.02a.307.307 0 0 1 0-.323Z"
                        />
                        <path
                            stroke="#A2A5C4"
                            stroke-linecap="round"
                            stroke-width="1.3"
                            d="m9.96 9.246-1.615 2.655a.307.307 0 0 0 0 .322l1.616 2.654m.159-6.13L8.502 6.093a.307.307 0 0 1 0-.322l1.616-2.655a.37.37 0 0 1 .318-.17h3.208a.37.37 0 0 1 .318.17l1.616 2.655c.061.1.061.222 0 .322l-.85 1.413"
                        />
                        <path
                            stroke="#A2A5C4"
                            stroke-linecap="round"
                            d="M14.906 1.661 13.71 3.08"
                        />
                        <path
                            fill="#A2A5C4"
                            d="M11.563 9.3a.6.6 0 0 1 .6-.6h.256a.6.6 0 0 1 .6.6v7.773h4.7a.6.6 0 0 1 .6.6v.054a.6.6 0 0 1-.6.6h-5.557a.6.6 0 0 1-.6-.6V9.3Z"
                        />
                    </svg>
                    <!-- <Tooltip trigger={['hover', 'click']} title="Select Proteins" placement="bottom"> -->
                    <!-- </Tooltip> -->
                    <div class="uni-view-horizontal-toolbar-subtitle">
                        Ligand
                    </div>
                </div>

                <div class="uni-view-horizontal-toolbar-item">
                    <svg
                        on:click={() => quickSelect(HierarchyType.Solvent)}
                        style="margin-left: 5"
                        class="uni-view-horizontal-toolbar-icon uni-view-horizontal-toolbar-dropdown"
                        xmlns="http://www.w3.org/2000/svg"
                        width="1em"
                        height="1em"
                        fill="none"
                        viewBox="0 0 20 20"
                    >
                        <path
                            stroke="#A2A5C4"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="1.3"
                            d="M8.636 14.942H2.315a.666.666 0 0 1-.667-.667v0c0-.174.069-.34.19-.465l1.654-1.692a1 1 0 0 1 .714-.3l4.423-.006m-4.848.011 2.474-2.53a1 1 0 0 0 .285-.699V2.665a1 1 0 0 1 1-1h2.192a1 1 0 0 1 1 1v4.503m-.003-2.708H8.633m2.096 2.097H8.633"
                        />
                        <path
                            fill="#A2A5C4"
                            d="M14.2 7.975c1.163 0 2.073.238 2.73.742.554.409.915.993 1.09 1.76.079.343-.203.648-.556.648h-.372c-.282 0-.52-.2-.615-.466-.148-.411-.362-.727-.652-.934-.392-.294-.952-.434-1.708-.434-.658 0-1.162.098-1.512.294-.434.224-.644.588-.644 1.092 0 .448.238.798.742 1.064.224.126.798.336 1.736.616 1.344.42 2.226.742 2.618.98.854.518 1.288 1.232 1.288 2.156 0 .896-.35 1.596-1.05 2.114-.7.504-1.68.756-2.94.756-1.218 0-2.17-.252-2.856-.728-.68-.485-1.104-1.196-1.28-2.136-.063-.341.216-.636.563-.636h.35c.299 0 .546.221.625.51.146.526.391.925.736 1.184.406.308 1.022.462 1.862.462.756 0 1.358-.14 1.806-.392.448-.252.672-.602.672-1.05 0-.56-.322-.994-.952-1.316-.224-.112-.882-.336-1.988-.672-1.232-.392-1.988-.658-2.296-.826-.77-.462-1.148-1.134-1.148-2.002 0-.882.364-1.568 1.106-2.072.7-.476 1.582-.714 2.646-.714Z"
                        />
                    </svg>
                    <!-- <Tooltip trigger={['hover', 'click']} title="Select Proteins" placement="bottom"> -->
                    <!-- </Tooltip> -->
                    <div class="uni-view-horizontal-toolbar-subtitle">
                        Solvent
                    </div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <KDropdown
                        on:change={(e) => {
                            surroundingVisible = e.detail;
                        }}
                        on:command={(e) => {
                            currGranularity = e.detail;
                            lightPlugin.managers.selection.structure.setGranularity(
                                e.detail,
                            );
                        }}
                        bind:this={surroundingDropdownRef}
                        trigger="click"
                    >
                        <div
                            class="row"
                            style={"flex-shrink: 0; align-items: center; justify-content: center;"}
                        >
                            <svg class="uni-view-horizontal-toolbar-icon {!selectionHistory ? 'disabled' : ''}" width="1em" height="1em" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M18.3346 10.0003C18.3346 5.39795 14.6037 1.66699 10.0013 1.66699C5.39893 1.66699 1.66797 5.39795 1.66797 10.0003C1.66797 14.6027 5.39893 18.3337 10.0013 18.3337"
                                    stroke="#A2A5C4"
                                    stroke-width="1.3"
                                    stroke-linecap="round"
                                />
                                <path
                                    d="M10 12C11.1046 12 12 11.1046 12 10C12 8.89543 11.1046 8 10 8C8.89543 8 8 8.89543 8 10C8 11.1046 8.89543 12 10 12Z"
                                    fill="#A2A5C4"
                                    stroke="#A2A5C4"
                                    stroke-width="1.3"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                />
                                <path
                                    fill-rule="evenodd"
                                    clip-rule="evenodd"
                                    d="M13 13L19 14.2L17.2 15.4L19 17.2L17.2 19L15.4 17.2L14.2 19L13 13Z"
                                    stroke="#A2A5C4"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                />
                            </svg>
                        </div>
                        <div slot="dropdown">
                            <div class="uni-view-horizontal-toolbar-surrounding-container">
                                <div style="color: #888BAB;">
                                    By Radius
                                    <svg style="margin-left: 6px" width="1em" height="1em" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M14 0H0v14h14V0z" fill="#fff" fill-opacity=".01" />
                                        <path
                                            d="M6.997 12.833c1.611 0 3.07-.653 4.125-1.709A5.815 5.815 0 0 0 12.831 7c0-1.61-.653-3.069-1.709-4.124a5.815 5.815 0 0 0-4.125-1.709c-1.61 0-3.069.653-4.124 1.709a5.815 5.815 0 0 0-1.709 4.124c0 1.611.653 3.07 1.709 4.125a5.815 5.815 0 0 0 4.124 1.709z"
                                            stroke="#A2A5C4"
                                            stroke-width="1.3"
                                            stroke-linejoin="round"
                                        />
                                        <path
                                            fill-rule="evenodd"
                                            clip-rule="evenodd"
                                            d="M7.003 3.209a.73.73 0 1 1 0 1.458.73.73 0 0 1 0-1.458z"
                                            fill="#A2A5C4"
                                        />
                                        <path
                                            d="M7.146 9.917V5.834h-.584M6.125 9.916h2.042"
                                            stroke="#A2A5C4"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                        />
                                    </svg>
                                    <!-- <Tooltip
                                        trigger={['hover', 'click']}
                                        overlay={'Expand Selection by Radius and Include Full Residue.'}
                                    > -->
                                    <!-- </Tooltip> -->
                                </div>
                                <div>
                                    <Textfield
                                        bind:value={surroundingRadius}
                                        label="Number with Step"
                                        type="number"
                                        input$step="1"
                                        suffix="Å"
                                        style="color: #000000"
                                    />
                                    <!-- <DpInputNumber
                                        onChange={value => setSurroundingRadius(value)}
                                        value={surroundingRadius}
                                        style={{ width: 190, border: '1px solid transparent' }}
                                        min={1}
                                        step={1}
                                        className="mr8"
                                        addonAfter="Å"
                                    /> -->
                                </div>
                                <div class="horizontal-split" style="margin: 12px 0;" />
                                <div style="color: #888BAB;margin-bottom:8px;">Select Structures</div>
                                <div class="row" style="flex-direction: column;align-items: center; justify-content: space-between;font-size: 12px; color: #000 !important;">
                                    <KRadioGroup value={expandFilter} on:updateValue={e => expandFilter = e.detail}>
                                        <KRadio uid={ExpandFilter.All}>All</KRadio>
                                        <KRadio uid={ExpandFilter.Residues}>Residues</KRadio>
                                        <KRadio uid={ExpandFilter.Water}>Water</KRadio>
                                        <KRadio uid={ExpandFilter.SolventWithoutWater}>Solvent Other Than Water</KRadio>
                                        <KRadio uid={ExpandFilter.Solvent}>All Solvent</KRadio>
                                    </KRadioGroup>
                                </div>
                                <div class="horizontal-split" style="margin: 12px 0" />
                                <div style="color: #888BAB;margin-bottom:8px;">Other Settings</div>
                                <div class="row" style="flex-direction: column;align-items: center; justify-content: space-between;font-size: 12px; color: #000 !important;">
                                    <KRadioGroup value={asWholeResidueState} on:updateValue={e => asWholeResidueState = e.detail}>
                                        <KRadio uid={1}>Include full residues</KRadio>
                                        <KRadio uid={0}>Include atoms</KRadio>
                                    </KRadioGroup>
                                </div>
                                <div class="horizontal-split" style="margin: 12px 0" />
                                <div class="row" style="align-items: center;justify-content: start;">
                                    <Checkbox bind:checked={excludeSelectedAtoms} />
                                    Exclude Selected Atoms
                                </div>
                                <div class="row" style="align-items: center;justify-content: end;">
                                    <button on:click={() => {
                                        lightPlugin.managers.selection.structure.expand({
                                            radius: surroundingRadius,
                                            asWholeResidue: asWholeResidueState,
                                            filter: expandFilter,
                                            excludeSelectedAtoms,
                                        });
                                        surroundingVisible = false;
                                        surroundingDropdownRef.handleClose();
                                    }}>
                                        Confirm
                                    </button>
                                </div>
                            </div>
                        </div>
                    </KDropdown>
                    <div class="uni-view-horizontal-toolbar-subtitle">
                        Expand
                    </div>
                </div>
            </div>
        </div>
        <div class="vertical-split" />
        <!-- Chem Assist -->
        <div style="margin: 4px 8px;">
            <div
                class="uni-view-horizontal-toolbar-title row"
            >
                Chem Assist
            </div>
            <div class="row">
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Measure</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item large">
                    <div class="uni-view-horizontal-toolbar-subtitle">Interaction</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Label</div>
                </div>
            </div>
        </div>

        <div class="vertical-split" />
        <!-- Style -->
        <div style="margin: 4px 8px;">
            <div
                class="uni-view-horizontal-toolbar-title row"
            >
                Style
            </div>
            <div class="row">
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Surface</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Ribbon</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Line</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Stick</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Ball&Stick</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">CPK</div>
                </div>
            </div>
        </div>
        <div class="vertical-split" />
        <!-- 3D Control -->
        <div style="margin: 4px 8px;">
            <div
                class="uni-view-horizontal-toolbar-title row"
            >
                3D Control
            </div>
            <div class="row">
                <div class="uni-view-horizontal-toolbar-item large">
                    <div class="uni-view-horizontal-toolbar-subtitle">Hydrogen</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Edit</div>
                </div>
                <div class="uni-view-horizontal-toolbar-item">
                    <div class="uni-view-horizontal-toolbar-subtitle">Setting</div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .row {
        display: flex;
        flex-flow: row wrap;
    }
    .uni-view-horizontal-toolbar-container {
        position: absolute;
        top: 24px;
        left: 50%;
        transform: translateX(-50%);
        background-color: #ffffff;
        box-shadow:
            0px 6px 10px rgba(183, 192, 231, 0.1),
            0px 8px 12px 1px rgba(170, 181, 223, 0.05);
        border-radius: 4px;
        z-index: 999;
        display: flex;
        color: #000000;
    }
    .fixed-right {
        left: auto;
        right: 0;
        transform: none;
    }
    .uni-view-horizontal-toolbar-inner {
        transition: all 0.2s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        overflow: hidden;
        flex-wrap: nowrap;
    }
    .uni-view-horizontal-toolbar-title {
        color: #b1b4d3;
        font-size: 8px;
        margin-bottom: 6px;
        justify-content: center;
    }
    .uni-view-horizontal-toolbar-item {
        width: 30px;
        height: 30px;
        position: relative;
    }
    .uni-view-horizontal-toolbar-item:not(:last-child) {
        margin-right: 8px;
    }
    .uni-view-horizontal-toolbar-item.large {
        width: 40px;
    }
    .uni-view-horizontal-toolbar-subtitle {
        color: #888bab;
        font-size: 8px;
        height: 12px;
        line-height: 12px;
        width: 100%;
        text-align: center;
        position: absolute;
        left: 0;
        bottom: 0;
    }
    .normal-icon {
        font-size: 16px !important;
        cursor: pointer;
        color: #a2a5c4 !important;
    }
    .uni-view-horizontal-toolbar-icon {
        margin: 0 !important;
        font-size: 16px;
        cursor: pointer;
        color: #a2a5c4 !important;
    }
    .uni-view-horizontal-toolbar-icon.disabled {
        color: #d6d8ef;
    }
    .uni-view-horizontal-toolbar-dropdown {
        width: 100%;
        height: 18px;
        text-align: center;
        position: absolute;
        left: 0;
        top: 0;
    }
    .uni-view-horizontal-toolbar-dropdown .normal-icon {
        font-size: 16px !important;
        cursor: pointer;
        color: #a2a5c4 !important;
    }
    .uni-view-horizontal-toolbar-surrounding-container {
        width: 214px;
        font-size: 12px !important;
        margin-top: 10px;
        background-color: #FFFFFF;
        padding: 12px;
        box-shadow: 0px 4px 7px rgba(155, 161, 184, 0.2), 0px 6px 10px 1px rgba(155, 161, 184, 0.1);
        border-radius: 4px;
    }
    .vertical-split {
        padding-left: 1px;
        height: 30px;
        background-color: #E9EBF7;
    }
    .horizontal-split {
        padding-top: 1px;
        background-color: #E9EBF7;
    }
</style>
