#svelte 

# Svelte Google Auth

- **Ставим либу**: https://github.com/beyonk-adventures/svelte-social-auth
- **Получаем google client id**: как получить - написано в [js-g-auth](js-g-auth.md)
- **Делаем виджет**:

```html
<script lang="ts">
  import { GoogleAuth } from "@beyonk/svelte-social-auth";
  const GOOGLE_CLIENT_ID =
    "643332836412-964d72e72d053d501f2949969849b96c.apps.googleusercontent.com";
</script>

<GoogleAuth
  clientId={GOOGLE_CLIENT_ID}
  on:auth-success={(e) => console.dir(e.detail.user)}
>
	<button>Войти</button>
</GoogleAuth>
```

## Траблшутинг

- В случае ошибки `Unknown file extension ".svelte" for ...` фиксим так:
	- https://www.reddit.com/r/sveltejs/comments/v0mx4i/typeerror_unknown_file_extension_svelte/
	- В `vite.config.js` правим `optimizeDeps`:

```js
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  plugins: [sveltekit()],
  ...
  optimizeDeps: {
    exclude: ['svelte-social-auth']
  }
});
```

## Альтернативы

- https://github.com/HalfdanJ/svelte-google-auth - но чет оч замороченно: какие-то хуки, кучу файлов надо редачить и тд