<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div class="mb-6">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div>
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900">
						Inventory Management
					</h1>
					<p class="text-gray-600 text-sm md:text-base">
						Manage your clinic's inventory, supplies, and equipment
					</p>
				</div>
				<div class="flex gap-2">
					<button
						class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 flex items-center gap-2"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							></path>
						</svg>
						Export
					</button>
					<button
						class="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 flex items-center gap-2"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6v6m0 0v6m0-6h6m-6 0H6"
							></path>
						</svg>
						Add Item
					</button>
				</div>
			</div>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-6">
			<!-- Total Items -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between">
					<div>
						<p class="text-sm font-medium text-gray-600 mb-1">Total Items</p>
						<p class="text-2xl md:text-3xl font-bold text-gray-900">1,284</p>
						<p class="text-xs text-gray-500 mt-1">+24 items added this month</p>
					</div>
					<div class="p-3 bg-gray-100 rounded-lg">
						<svg
							class="w-6 h-6 text-gray-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
							></path>
						</svg>
					</div>
				</div>
			</div>

			<!-- Low Stock Items -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between">
					<div>
						<p class="text-sm font-medium text-gray-600 mb-1">Low Stock Items</p>
						<p class="text-2xl md:text-3xl font-bold text-gray-900">42</p>
						<p class="text-xs text-gray-500 mt-1">+6 from last month</p>
					</div>
					<div class="p-3 bg-orange-100 rounded-lg">
						<svg
							class="w-6 h-6 text-orange-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.232 16.5c-.77.833.192 2.5 1.732 2.5z"
							></path>
						</svg>
					</div>
				</div>
			</div>

			<!-- Value of Inventory -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between">
					<div>
						<p class="text-sm font-medium text-gray-600 mb-1">Value of Inventory</p>
						<p class="text-2xl md:text-3xl font-bold text-gray-900">$124,750</p>
						<p class="text-xs text-gray-500 mt-1">+12.5% from last month</p>
					</div>
					<div class="p-3 bg-gray-100 rounded-lg">
						<svg
							class="w-6 h-6 text-gray-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 3h2l.4 2M7 13h10l4-8H5.4m2.6 10l-1.6-8m1.6 8a2 2 0 11-4 0 2 2 0 014 0zm9 0a2 2 0 11-4 0 2 2 0 014 0z"
							></path>
						</svg>
					</div>
				</div>
			</div>

			<!-- Active Suppliers -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between">
					<div>
						<p class="text-sm font-medium text-gray-600 mb-1">Active Suppliers</p>
						<p class="text-2xl md:text-3xl font-bold text-gray-900">38</p>
						<p class="text-xs text-gray-500 mt-1">View all suppliers</p>
					</div>
					<div class="p-3 bg-gray-100 rounded-lg">
						<svg
							class="w-6 h-6 text-gray-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
							></path>
						</svg>
					</div>
				</div>
			</div>
		</div>

		<!-- Inventory Table -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200">
			<!-- Table Header with Search and Filters -->
			<div class="p-4 md:p-6 border-b border-gray-200">
				<div class="flex flex-col lg:flex-row lg:items-center gap-4">
					<!-- Search -->
					<div class="relative flex-1 max-w-md">
						<svg
							class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
							></path>
						</svg>
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search inventory..."
							class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						/>
					</div>

					<!-- Filters -->
					<div class="flex flex-wrap gap-2">
						<select
							v-model="selectedCategory"
							class="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						>
							<option value="">All Categories</option>
							<option value="Medical Supplies">Medical Supplies</option>
							<option value="Medications">Medications</option>
							<option value="Equipment">Equipment</option>
						</select>
						<select
							v-model="selectedStatus"
							class="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
						>
							<option value="">All Status</option>
							<option value="In Stock">In Stock</option>
							<option value="Low Stock">Low Stock</option>
							<option value="Out of Stock">Out of Stock</option>
							<option value="On Order">On Order</option>
						</select>
						<button class="p-2 border border-gray-300 rounded-lg hover:bg-gray-50">
							<svg
								class="w-4 h-4 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
								></path>
							</svg>
						</button>
					</div>
				</div>

				<!-- Category Tabs -->
				<div class="flex flex-wrap gap-1 mt-4">
					<button
						v-for="tab in tabs"
						:key="tab"
						@click="activeTab = tab"
						:class="[
							'px-4 py-2 text-sm font-medium rounded-lg transition-colors',
							activeTab === tab
								? 'bg-blue-100 text-blue-700'
								: 'text-gray-600 hover:text-gray-900 hover:bg-gray-100',
						]"
					>
						{{ tab }}
					</button>
				</div>
			</div>

			<!-- Table Content -->
			<div class="p-4 md:p-6">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Inventory Items</h3>
				<p class="text-sm text-gray-600 mb-4">Showing {{ filteredItems.length }} items</p>

				<!-- Desktop Table -->
				<div class="hidden md:block overflow-x-auto">
					<table class="w-full">
						<thead>
							<tr
								class="text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b border-gray-200"
							>
								<th class="pb-3">Item ID</th>
								<th class="pb-3">Name</th>
								<th class="pb-3">Category</th>
								<th class="pb-3">Stock Level</th>
								<th class="pb-3">Status</th>
								<th class="pb-3">Last Updated</th>
								<th class="pb-3">Actions</th>
							</tr>
						</thead>
						<tbody class="divide-y divide-gray-200">
							<tr
								v-for="item in filteredItems"
								:key="item.id"
								class="hover:bg-gray-50"
							>
								<td class="py-4 text-sm font-mono text-gray-900">{{ item.id }}</td>
								<td class="py-4 text-sm font-medium text-gray-900">
									{{ item.name }}
								</td>
								<td class="py-4 text-sm text-gray-600">{{ item.category }}</td>
								<td class="py-4 text-sm text-gray-900">
									{{ item.currentStock }} / {{ item.maxStock }}
								</td>
								<td class="py-4">
									<span
										:class="getStatusClass(item.status)"
										class="inline-flex px-2 py-1 text-xs font-medium rounded-full"
									>
										{{ item.status }}
									</span>
								</td>
								<td class="py-4 text-sm text-gray-600">{{ item.lastUpdated }}</td>
								<td class="py-4">
									<button class="text-gray-400 hover:text-gray-600">
										<svg
											class="w-4 h-4"
											fill="none"
											stroke="currentColor"
											viewBox="0 0 24 24"
										>
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												stroke-width="2"
												d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
											></path>
										</svg>
									</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>

				<!-- Mobile Cards -->
				<div class="md:hidden space-y-4">
					<div
						v-for="item in filteredItems"
						:key="item.id"
						class="bg-gray-50 rounded-lg p-4"
					>
						<div class="flex justify-between items-start mb-2">
							<div>
								<h4 class="font-medium text-gray-900">{{ item.name }}</h4>
								<p class="text-sm text-gray-600">{{ item.id }}</p>
							</div>
							<span
								:class="getStatusClass(item.status)"
								class="inline-flex px-2 py-1 text-xs font-medium rounded-full"
							>
								{{ item.status }}
							</span>
						</div>
						<div class="grid grid-cols-2 gap-4 text-sm">
							<div>
								<p class="text-gray-600">Category</p>
								<p class="font-medium">{{ item.category }}</p>
							</div>
							<div>
								<p class="text-gray-600">Stock Level</p>
								<p class="font-medium">
									{{ item.currentStock }} / {{ item.maxStock }}
								</p>
							</div>
						</div>
						<div class="mt-3 text-xs text-gray-500">
							Last updated: {{ item.lastUpdated }}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const searchQuery = ref('')
const selectedCategory = ref('')
const selectedStatus = ref('')
const activeTab = ref('All Items')

// Tabs
const tabs = ['All Items', 'Medications', 'Medical Supplies', 'Equipment']

// Sample inventory data
const inventoryItems = ref([
	{
		id: 'INV001',
		name: 'Disposable Gloves (Box)',
		category: 'Medical Supplies',
		currentStock: 45,
		maxStock: 20,
		status: 'In Stock',
		lastUpdated: '2023-04-15',
	},
	{
		id: 'INV002',
		name: 'Ibuprofen 200mg',
		category: 'Medications',
		currentStock: 12,
		maxStock: 15,
		status: 'Low Stock',
		lastUpdated: '2023-04-14',
	},
	{
		id: 'INV003',
		name: 'Blood Pressure Monitor',
		category: 'Equipment',
		currentStock: 5,
		maxStock: 3,
		status: 'In Stock',
		lastUpdated: '2023-04-10',
	},
	{
		id: 'INV004',
		name: 'Surgical Masks (Box)',
		category: 'Medical Supplies',
		currentStock: 0,
		maxStock: 10,
		status: 'Out of Stock',
		lastUpdated: '2023-04-12',
	},
	{
		id: 'INV005',
		name: 'Amoxicillin 500mg',
		category: 'Medications',
		currentStock: 8,
		maxStock: 10,
		status: 'Low Stock',
		lastUpdated: '2023-04-13',
	},
	{
		id: 'INV006',
		name: 'Syringes 5ml',
		category: 'Medical Supplies',
		currentStock: 120,
		maxStock: 50,
		status: 'In Stock',
		lastUpdated: '2023-04-11',
	},
	{
		id: 'INV007',
		name: 'Examination Table Paper',
		category: 'Medical Supplies',
		currentStock: 3,
		maxStock: 5,
		status: 'Low Stock',
		lastUpdated: '2023-04-09',
	},
	{
		id: 'INV008',
		name: 'Digital Thermometer',
		category: 'Equipment',
		currentStock: 15,
		maxStock: 5,
		status: 'In Stock',
		lastUpdated: '2023-04-08',
	},
	{
		id: 'INV009',
		name: 'Alcohol Swabs (Box)',
		category: 'Medical Supplies',
		currentStock: 25,
		maxStock: 20,
		status: 'On Order',
		lastUpdated: '2023-04-07',
	},
	{
		id: 'INV010',
		name: 'Paracetamol 500mg',
		category: 'Medications',
		currentStock: 60,
		maxStock: 30,
		status: 'In Stock',
		lastUpdated: '2023-04-06',
	},
])

// Computed filtered items
const filteredItems = computed(() => {
	let items = inventoryItems.value

	// Filter by search query
	if (searchQuery.value) {
		items = items.filter(
			(item) =>
				item.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
				item.id.toLowerCase().includes(searchQuery.value.toLowerCase()),
		)
	}

	// Filter by category
	if (selectedCategory.value) {
		items = items.filter((item) => item.category === selectedCategory.value)
	}

	// Filter by status
	if (selectedStatus.value) {
		items = items.filter((item) => item.status === selectedStatus.value)
	}

	// Filter by active tab
	if (activeTab.value !== 'All Items') {
		items = items.filter((item) => item.category === activeTab.value)
	}

	return items
})

// Status styling helper
const getStatusClass = (status) => {
	switch (status) {
		case 'In Stock':
			return 'bg-green-100 text-green-800'
		case 'Low Stock':
			return 'bg-yellow-100 text-yellow-800'
		case 'Out of Stock':
			return 'bg-red-100 text-red-800'
		case 'On Order':
			return 'bg-blue-100 text-blue-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>
