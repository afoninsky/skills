<script setup lang="ts">
defineProps<{ title: string }>();
</script>

<template>
  <article class="goal-card">
    <h2>{{ title }}</h2>
  </article>
</template>

<style scoped>
.goal-card {
  padding: var(--space-card);
  border-radius: var(--radius-card);
  background: var(--surface-raised);
}
</style>

