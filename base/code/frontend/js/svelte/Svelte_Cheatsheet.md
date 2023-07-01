#svelte #js #cheatsheet

# Svelte Cheatsheet

## Binding & event handling

```html
<!-- 1D binding -->
<Component field={field} />
<Component {field} />

<!-- 2D binding-->
<Component bind:field={field} />
<Component bind:field />
<!-- useful for inputs -->
<input bind:value={val}>

<!-- Events -->
<Component on:click={click} />
```

## Blocks

### `if` - conditional rendering

```html
{#if condition1}
	<!-- condition1 rendering -->
{:else if condition2}
	<!-- condition2 rendering -->
{:else}
	<!-- else rendering -->
{/if}

```

### `each` — iteration / for loop rendering

```html
<!-- Regular -->
{#each array as item}
	<!-- item rendering -->
{/each}

<!-- each with index -->
{#each array as item, index}
	<!-- item w/ index rendering -->
{/each}

<!-- each for pairs -->
{#each pairs as [item1, item2]}
	<!-- pair rendering -->
{/each}

<!-- each for object -->
{#each Object.entries({a: 1, b:2}) as [key, value]}
	<!-- object entry rendering -->
{/each}
```

### `await` - promise rendering

```html
{#await promise}
	<!-- loading -->
{:then data}
	<!-- render promise data -->
<!-- optional -->
{:catch err}
	<!-- render promise err -->
{/await}
```

## Computed

```html
<script>
	// Computed property 
	$: tag = browser ? $page.url.searchParams.get("tag") : null;
	
	// Computed block 
	$: {
		console.log(tag)
	}
</script>
```

## Components

### Props / binding

```html
<!-- A.svelte -->
<script>
	export let href;
</script>

<a {href}></a>

<!-- Page.svelte -->
<A href="https://ya.ru" /> 
```

#### Class binding

```html
<!-- Component.svelte -->
<script>  
    let class_ = '';
    export {class_ as class}
</script>

<div class={class_}>...</div>
<div class={`... ${class_}`}>...</div>

<!-- Page.svelte -->
<Component class='text-lg' />
```

### Event forwarding / dispatching

```html
<!-- Button.svelte -->
<script>
    import {createEventDispatcher} from "svelte";  

    const dispatch = createEventDispatcher();

    function click(e) {dispatch('click')}
</script>

<button on:click={click} />  

<!-- Page.svelte -->
<Button on:click={click}>

<!-- OR -->

<!-- Button.svelte -->
<script>
	export let action;
</script>

<button on:click={action} />  

<!-- Page.svelte -->
<Button action={click}>
```

### Slots

```html
<!-- A.svelte -->
<a>
	<slot />
</a>

<!-- Page.svelte -->
<A>Link</A>
```

## Page 

### Query params

```html
<script>
	import { browser } from "$app/environment";
	import { page } from "$app/stores";

	// browser = client-side code
	$: tag = browser ? $page.url.searchParams.get("tag") : null;
</script>
```

### Redirect

```html
<script>
	import { goto } from "$app/navigation";
	
	function redirect() {
		goto('/')
	}
</script>

<button on:click={redirect} />
```