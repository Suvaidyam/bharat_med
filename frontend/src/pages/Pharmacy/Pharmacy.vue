<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8">
			<div>
				<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">Medicine List</h1>
				<p class="text-gray-600">
					Manage and view all medicines in the pharmacy inventory
				</p>
			</div>
			<button
				class="mt-4 sm:mt-0 bg-gray-900 text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-gray-800 transition-colors"
			>
				<span class="text-lg">+</span>
				Add New Medicine
			</button>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-8">
			<!-- Total Medicines -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
						<svg
							class="w-5 h-5 text-blue-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.781 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 9.172V5L8 4z"
							/>
						</svg>
					</div>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Total Medicines</p>
					<p class="text-2xl font-bold text-gray-900">1,248</p>
				</div>
				<p class="text-xs text-gray-500">+24 added this month</p>
			</div>

			<!-- Low Stock Items -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div
						class="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center"
					>
						<div
							class="w-6 h-6 bg-orange-500 rounded-full flex items-center justify-center"
						>
							<span class="text-white text-xs font-bold">!</span>
						</div>
					</div>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Low Stock Items</p>
					<p class="text-2xl font-bold text-gray-900">42</p>
				</div>
				<p class="text-xs text-gray-500">Need reordering soon</p>
			</div>

			<!-- Expiring Soon -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center">
						<div
							class="w-6 h-6 bg-red-500 rounded-full flex items-center justify-center"
						>
							<span class="text-white text-xs font-bold">!</span>
						</div>
					</div>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Expiring Soon</p>
					<p class="text-2xl font-bold text-gray-900">18</p>
				</div>
				<p class="text-xs text-gray-500">Within next 30 days</p>
			</div>

			<!-- Categories -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div
						class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center"
					>
						<svg
							class="w-5 h-5 text-purple-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
							/>
						</svg>
					</div>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Categories</p>
					<p class="text-2xl font-bold text-gray-900">36</p>
				</div>
				<p class="text-xs text-gray-500">Medicine categories</p>
			</div>
		</div>

		<!-- Search and Filters -->
		<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100 mb-6">
			<div class="flex flex-col lg:flex-row gap-4">
				<!-- Search -->
				<div class="flex-1">
					<div class="relative">
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
							/>
						</svg>
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search medicines..."
							class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
						/>
					</div>
				</div>

				<!-- Filters -->
				<div class="flex flex-col sm:flex-row gap-4">
					<select
						v-model="selectedCategory"
						class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none min-w-[150px]"
					>
						<option value="">All Categories</option>
						<option value="Antibiotics">Antibiotics</option>
						<option value="Analgesics">Analgesics</option>
						<option value="Antidiabetics">Antidiabetics</option>
						<option value="Antihypertensives">Antihypertensives</option>
						<option value="Antihistamines">Antihistamines</option>
					</select>

					<select
						v-model="selectedStatus"
						class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none min-w-[120px]"
					>
						<option value="">All Status</option>
						<option value="In Stock">In Stock</option>
						<option value="Low Stock">Low Stock</option>
						<option value="Out of Stock">Out of Stock</option>
					</select>
				</div>
			</div>

			<!-- Filter Tabs -->
			<div class="flex gap-6 mt-6 border-b border-gray-200">
				<button
					v-for="tab in tabs"
					:key="tab"
					@click="activeTab = tab"
					:class="[
						'pb-2 px-1 text-sm font-medium border-b-2 transition-colors',
						activeTab === tab
							? 'text-blue-600 border-blue-600'
							: 'text-gray-500 border-transparent hover:text-gray-700',
					]"
				>
					{{ tab }}
				</button>
			</div>
		</div>

		<!-- Medicine Table -->
		<div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
			<!-- Desktop Table -->
			<div class="hidden lg:block overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								ID
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Medicine Name
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Category
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Stock
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Expiry Date
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Actions
							</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-gray-200">
						<tr
							v-for="medicine in filteredMedicines"
							:key="medicine.id"
							class="hover:bg-gray-50"
						>
							<td class="py-4 px-6 text-sm text-gray-600">{{ medicine.id }}</td>
							<td class="py-4 px-6">
								<div>
									<p class="text-sm font-medium text-gray-900">
										{{ medicine.name }}
									</p>
									<p class="text-xs text-gray-500">{{ medicine.genericName }}</p>
								</div>
							</td>
							<td class="py-4 px-6 text-sm text-gray-600">
								{{ medicine.category }}
							</td>
							<td class="py-4 px-6 text-sm text-gray-600">{{ medicine.stock }}</td>
							<td class="py-4 px-6 text-sm text-gray-600">
								{{ medicine.expiryDate }}
							</td>
							<td class="py-4 px-6">
								<span
									:class="getStatusClass(medicine.status)"
									class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
								>
									{{ medicine.status }}
								</span>
							</td>
							<td class="py-4 px-6">
								<button class="text-gray-400 hover:text-gray-600">
									<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
										<path
											d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
										/>
									</svg>
								</button>
							</td>
						</tr>
					</tbody>
				</table>
			</div>

			<!-- Mobile Cards -->
			<div class="lg:hidden">
				<div
					v-for="medicine in filteredMedicines"
					:key="medicine.id"
					class="p-4 border-b border-gray-200 last:border-b-0"
				>
					<div class="flex justify-between items-start mb-3">
						<div class="flex-1">
							<h3 class="text-sm font-medium text-gray-900">{{ medicine.name }}</h3>
							<p class="text-xs text-gray-500">{{ medicine.genericName }}</p>
							<p class="text-xs text-gray-500 mt-1">{{ medicine.id }}</p>
						</div>
						<span
							:class="getStatusClass(medicine.status)"
							class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ml-2"
						>
							{{ medicine.status }}
						</span>
					</div>

					<div class="grid grid-cols-2 gap-4 text-xs">
						<div>
							<p class="text-gray-500">Category</p>
							<p class="text-gray-900 font-medium">{{ medicine.category }}</p>
						</div>
						<div>
							<p class="text-gray-500">Stock</p>
							<p class="text-gray-900 font-medium">{{ medicine.stock }}</p>
						</div>
						<div>
							<p class="text-gray-500">Expiry Date</p>
							<p class="text-gray-900 font-medium">{{ medicine.expiryDate }}</p>
						</div>
						<div class="flex justify-end">
							<button class="text-gray-400 hover:text-gray-600">
								<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
									<path
										d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
									/>
								</svg>
							</button>
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
const activeTab = ref('All')

const tabs = ['All', 'Prescription', 'OTC', 'Controlled']

const medicines = ref([
	{
		id: 'MED001',
		name: 'Amoxicillin 500mg',
		genericName: 'Amoxicillin',
		category: 'Antibiotics',
		stock: '1250 units',
		expiryDate: '2025-06-15',
		status: 'In Stock',
	},
	{
		id: 'MED002',
		name: 'Paracetamol 500mg',
		genericName: 'Acetaminophen',
		category: 'Analgesics',
		stock: '3500 units',
		expiryDate: '2025-08-22',
		status: 'In Stock',
	},
	{
		id: 'MED003',
		name: 'Metformin 850mg',
		genericName: 'Metformin HCl',
		category: 'Antidiabetics',
		stock: '850 units',
		expiryDate: '2024-12-10',
		status: 'In Stock',
	},
	{
		id: 'MED004',
		name: 'Lisinopril 10mg',
		genericName: 'Lisinopril',
		category: 'Antihypertensives',
		stock: '120 units',
		expiryDate: '2024-09-30',
		status: 'Low Stock',
	},
	{
		id: 'MED005',
		name: 'Morphine 15mg',
		genericName: 'Morphine Sulfate',
		category: 'Analgesics',
		stock: '75 units',
		expiryDate: '2024-11-05',
		status: 'Low Stock',
	},
	{
		id: 'MED006',
		name: 'Cetirizine 10mg',
		genericName: 'Cetirizine HCl',
		category: 'Antihistamines',
		stock: '0 units',
		expiryDate: '2025-03-18',
		status: 'Out of Stock',
	},
])

// Computed properties
const filteredMedicines = computed(() => {
	return medicines.value.filter((medicine) => {
		const matchesSearch =
			medicine.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			medicine.genericName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			medicine.id.toLowerCase().includes(searchQuery.value.toLowerCase())

		const matchesCategory =
			!selectedCategory.value || medicine.category === selectedCategory.value
		const matchesStatus = !selectedStatus.value || medicine.status === selectedStatus.value

		return matchesSearch && matchesCategory && matchesStatus
	})
})

// Methods
const getStatusClass = (status) => {
	switch (status) {
		case 'In Stock':
			return 'bg-green-100 text-green-800'
		case 'Low Stock':
			return 'bg-yellow-100 text-yellow-800'
		case 'Out of Stock':
			return 'bg-red-100 text-red-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>
