<script setup lang="ts">
import NavMain from '@/components/sidebar/NavMain.vue'
import NavProjects from '@/components/sidebar/NavProjects.vue'

import type { SidebarProps } from '../ui/sidebar'

import {
  Settings2,
  Bitcoin,
  ChartCandlestick,
  CircleDollarSign,
  Github,
  Book,
} from "lucide-vue-next"

import {
  Sidebar,
  SidebarContent,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
  SidebarHeader,
  SidebarRail,
} from '../ui/sidebar'

const props = withDefaults(defineProps<SidebarProps>(), {
  collapsible: "icon",
})

const data = {
  navMain: [
    {
      title: "Crypto",
      url: "/crypto/market",
      icon: Bitcoin,
      isActive: true,
      items: [
        {
          title: "Market",
          url: "/crypto/market",
          meta: { breadcrumb: ["Crypto", "Market"] },
        },
        {
          title: "QI Invest",
          url: "#",
        },
        {
          title: "Demo Trade",
          url: "#",
        },
      ],
    },
    {
      title: "Stocks",
      url: "#",
      icon: ChartCandlestick,
      items: [
        {
          title: "Market",
          url: "#",
        },
        {
          title: "QI Invest",
          url: "#",
        },
        {
          title: "Demo Trade",
          url: "#",
        },
      ],
    },
    {
      title: "Settings",
      url: "#",
      icon: Settings2,
      items: [
        {
          title: "General",
          url: "#",
        },
        {
          title: "API",
          url: "#",
        },
      ],
    },
  ],
  projects: [
    {
      name: "Documentation",
      url: "#",
      icon: Book,
    },
    {
      name: "GitHub",
      url: "#",
      icon: Github,
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton size="lg" as-child>
            <a href="/dashboad">
              <div
                class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <CircleDollarSign class="size-4" />
              </div>
              <div class="grid flex-1 text-left text-sm leading-tight">
                <span class="truncate font-semibold">GoTrade</span>
                <span class="truncate text-xs">Investments</span>
              </div>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <NavProjects :projects="data.projects" />
    </SidebarContent>
    <SidebarRail />
  </Sidebar>
</template>
