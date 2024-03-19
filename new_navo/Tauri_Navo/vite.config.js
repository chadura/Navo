import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from 'path';

export default defineConfig(async () => ({
  plugins: [vue()],
  optimizeDeps: {
    include: ["@vue/runtime-core"],
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, "src/index.hmtl"),
          home: path.resolve(__dirname, "src/List.html"),
        },
      },
    },
  },

  clearScreen: false,
  server: {
    port: 1420,
    strictPort: true,
    watch: {
      // 3. tell vite to ignore watching `src-tauri`
      ignored: ["**/src-tauri/**"],
    },
  },
}));
