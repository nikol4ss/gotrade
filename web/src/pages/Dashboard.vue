<script setup lang="ts">
import { DollarSign, CreditCard, PieChart, TrendingUp, Activity, AlertCircle, MapPin, Star } from 'lucide-vue-next';
import Quotation from '@/components/charts/Quotation.vue';
import AreaChart from '@/components/charts/AreaChart.vue';
import DonutChart from '@/components/charts/DonutChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
</script>

<template>
  <div class="flex flex-1 flex-col gap-6 p-4">

    <!-- Linha 1: Saldo e Gastos -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <DollarSign class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Saldo Total</h2>
        </div>
        <span class="text-2xl font-bold">$123,456</span>
        <span class="text-sm text-muted-foreground mt-1">Total de todos os investimentos</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <CreditCard class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Gastos</h2>
        </div>
        <span class="text-2xl font-bold">$5,432</span>
        <span class="text-sm text-muted-foreground mt-1">Gastos nos últimos 30 dias</span>
      </div>
    </div>

    <!-- Linha 2: Distribuição por Ativos/Setores -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <PieChart class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Distribuição por Ativos</h2>
      </div>
      <DonutChart class="flex-1 w-full h-72 md:h-96" />
    </div>

    <!-- Linha 3: Performance de Carteira -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Performance de Carteira</h2>
      </div>
      <AreaChart class="flex-1 w-full h-72 md:h-96" />
    </div>

    <!-- Linha 4: Cotações e Avaliação + Indicadores de Risco -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <Activity class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Cotações e Avaliação</h2>
        </div>
        <Quotation class="flex-1 w-full h-72 md:h-96" />
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <Star class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Indicadores de Risco</h2>
        </div>
        <span class="text-muted-foreground">Volatilidade, correlação, liquidez...</span>
      </div>
    </div>

    <!-- Linha 5: Tendência de Investimentos -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <TrendingUp class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Tendência de Investimentos</h2>
      </div>
      <LineChart class="flex-1 w-full h-72 md:h-96" />
    </div>

    <!-- Linha 6: Feedback / Recomendações -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-64">
      <div class="flex items-center gap-2 mb-2">
        <AlertCircle class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Feedback e Recomendações</h2>
      </div>
      <div class="flex-1 rounded-xl bg-muted/30 flex items-center justify-center">
        <span class="text-muted-foreground">Sugestões de ajustes e alertas futuros</span>
      </div>
    </div>

    <!-- Linha 7: Retorno Mensal / ROI -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
      <div class="flex items-center gap-2 mb-2">
        <DollarSign class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Retorno Mensal / ROI</h2>
      </div>
      <span class="text-muted-foreground">Ganho líquido por tipo de investimento</span>
    </div>

    <!-- Linha 8: Top Ativos / Maiores Performers + Alocação por Risco -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <Star class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Top Ativos</h2>
        </div>
        <span class="text-muted-foreground">Maiores valorizados e depreciados</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <PieChart class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Alocação por Risco</h2>
        </div>
        <span class="text-muted-foreground">Baixo, Médio e Alto risco</span>
      </div>
    </div>

    <!-- Linha 9: Fluxo de Entradas e Saídas + Diversificação Geográfica -->
    <div class="grid gap-4 md:grid-cols-2">
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
        <div class="flex items-center gap-2 mb-2">
          <CreditCard class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Fluxo de Entradas e Saídas</h2>
        </div>
        <span class="text-muted-foreground">Aportes e retiradas recentes</span>
      </div>
      <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
        <div class="flex items-center gap-2 mb-2">
          <MapPin class="w-5 h-5"/>
          <h2 class="text-lg font-semibold">Diversificação Geográfica</h2>
        </div>
        <span class="text-muted-foreground">Distribuição por região/país</span>
      </div>
    </div>

    <!-- Linha 10: Alertas / Próximos Eventos -->
    <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-48">
      <div class="flex items-center gap-2 mb-2">
        <AlertCircle class="w-5 h-5"/>
        <h2 class="text-lg font-semibold">Alertas e Próximos Eventos</h2>
      </div>
      <span class="text-muted-foreground">Vencimentos, dividendos, eventos importantes</span>
    </div>

  </div>
</template>
