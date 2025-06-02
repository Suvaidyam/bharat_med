<template>
	<div class="w-screen h-screen flex overflow-hidden">
		<!-- Sidebar - Fixed width, full height -->
		<div class="hidden md:block flex-shrink-0">
			<Sidebar />
		</div>

		<!-- Main content area - Takes remaining width -->
		<div class="flex-1 flex flex-col min-w-0 overflow-hidden">
			<!-- Topbar - Fixed height -->
			<div class="flex-shrink-0">
				<Topbar />
			</div>

			<!-- Main content - Scrollable area -->
			<div class="flex-1 overflow-y-auto p-4 scrollbar-thumb-slate-800">
				<router-view />
			</div>
		</div>
	</div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
import Topbar from '@/components/Topbar.vue'
</script>
