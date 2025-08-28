<script setup lang="ts">
import { AreaChart as BaseAreaChart } from "@/components/ui/chart-area"
import { type PropType } from "vue"

interface ChartData {
  name: string
  [key: string]: number | string
}

const props = defineProps({
  data: { type: Array as PropType<ChartData[]>, required: true },
  categories: { type: Array as PropType<string[]>, required: true },
  colors: {
    type: Array as PropType<string[]>, default: () => ['#1E293B',
      '#475569',
      '#64748B',
      '#94A3B8',
      '#F1F5F9']
  }
})
</script>

<template>
  <BaseAreaChart :data="props.data" index="name" :categories="props.categories" :colors="props.colors" />
</template>
