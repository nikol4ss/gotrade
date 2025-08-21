<script setup lang="ts">
import AppSidebar from "@/components/sidebar/AppSidebar.vue"
import { SidebarInset, SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator } from "@/components/ui/breadcrumb"
import ToggleTheme from "@/components/ToggleTheme.vue"
import { useRoute } from "vue-router"
import { computed } from "vue"

const route = useRoute()

const crumbs = computed(() => {
  if (!route.meta.breadcrumb) return ["Dashboard"]
  return Array.isArray(route.meta.breadcrumb)
    ? route.meta.breadcrumb
    : [route.meta.breadcrumb]
})
</script>

<template>
  <SidebarProvider>
    <AppSidebar />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2">
        <div class="flex items-center gap-2 px-4">
          <SidebarTrigger class="-ml-1 cursor-pointer" />
          <Breadcrumb>
            <BreadcrumbList>
              <template v-for="(crumb, index) in crumbs" :key="index">
                <BreadcrumbItem>
                  <template v-if="index < crumbs.length - 1">
                    <BreadcrumbLink href="#">{{ crumb }}</BreadcrumbLink>
                  </template>
                  <template v-else>
                    <BreadcrumbPage>{{ crumb }}</BreadcrumbPage>
                  </template>
                </BreadcrumbItem>
                <BreadcrumbSeparator v-if="index < crumbs.length - 1" />
              </template>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
      </header>

      <div class="fixed top-5 right-5 z-50 flex items-center gap-4">
        <ToggleTheme />
      </div>

      <main class="p-4">
        <router-view />
      </main>
    </SidebarInset>
  </SidebarProvider>
</template>
