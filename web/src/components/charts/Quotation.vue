<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import type { PropType } from "vue"

interface Column {
  key: string
  label: string
  align?: "left" | "center" | "right"
}

defineProps({
  caption: { type: String, default: "" },
  data: { type: Array as PropType<Record<string, any>[]>, required: true },
  columns: { type: Array as PropType<Column[]>, required: true },
})
</script>

<template>
  <Table>
    <TableCaption v-if="caption">{{ caption }}</TableCaption>
    <TableHeader>
      <TableRow>
        <TableHead v-for="col in columns" :key="col.key"
          :class="col.align === 'center' ? 'text-center' : col.align === 'right' ? 'text-right' : 'text-left'">
          {{ col.label }}
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="(row, i) in data" :key="i">
        <TableCell v-for="col in columns" :key="col.key"
          :class="col.align === 'center' ? 'text-center font-medium' : col.align === 'right' ? 'text-right font-medium' : 'text-left font-medium'">
          {{ row[col.key] }}
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>
