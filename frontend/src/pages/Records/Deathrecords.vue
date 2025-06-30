<template>
	<div class="p-6 min-h-screen">
		<!-- Header -->
		<div class="flex justify-between items-start mb-6">
			<div>
				<h1 class="text-2xl font-bold">Death Records</h1>
				<p class="text-sm text-gray-500">
					Manage and track all death records in the system
				</p>
			</div>
			<div class="flex gap-2">
				<button
					class="flex items-center px-4 py-2 text-sm bg-white border rounded-sm hover:bg-gray-100"
				>
					<span class="material-icons text-base mr-1">file_download</span> Export
				</button>
				<button
					class="px-4 py-2 text-sm font-medium text-white bg-black rounded-sm hover:bg-gray-800"
				>
					+ Add Record
				</button>
			</div>
		</div>

		<!-- Tabs -->
		<div class="mb-4 flex border-b text-sm">
			<button class="px-4 py-2 font-medium border-b-2 border-black">All Records</button>
			<button class="px-4 py-2 text-gray-600 hover:text-black">Verified</button>
			<button class="px-4 py-2 text-gray-600 hover:text-black">Pending</button>
		</div>

		<!-- Search & Filter -->
		<div class="flex flex-col md:flex-row items-center gap-3 mb-4">
			<input
				type="text"
				placeholder="Search records..."
				class="w-full md:w-1/3 px-3 py-2 border rounded-sm"
				v-model="searchQuery"
			/>
			<button
				class="flex items-center px-3 py-2 border rounded-sm bg-white hover:bg-gray-100"
			>
				<span class="material-icons text-base mr-1">filter_list</span> Filter
			</button>
			<input type="date" class="px-3 py-2 border rounded-sm" v-model="filterDate" />
		</div>

		<!-- Records Table -->
		<div class="overflow-x-auto bg-white rounded shadow">
			<table class="w-full text-sm text-left border-t">
				<thead class="bg-gray-100 text-gray-700 uppercase">
					<tr>
						<th class="px-4 py-3">Record ID</th>
						<th class="px-4 py-3">Name</th>
						<th class="px-4 py-3">Age</th>
						<th class="px-4 py-3">Date of Death</th>
						<th class="px-4 py-3">Cause of Death</th>
						<th class="px-4 py-3">Status</th>
						<th class="px-4 py-3">Actions</th>
					</tr>
				</thead>
				<tbody>
					<tr
						v-for="record in filteredRecords"
						:key="record.id"
						class="border-t hover:bg-gray-50"
					>
						<td class="px-4 py-3">{{ record.id }}</td>
						<td class="px-4 py-3">{{ record.name }}</td>
						<td class="px-4 py-3">{{ record.age }}</td>
						<td class="px-4 py-3">{{ record.date }}</td>
						<td class="px-4 py-3">{{ record.cause }}</td>
						<td class="px-4 py-3">
							<span
								:class="[
									'px-2 py-1 rounded-full text-xs font-semibold',
									record.status === 'Verified'
										? 'bg-green-100 text-green-800'
										: 'bg-yellow-100 text-yellow-800',
								]"
							>
								{{ record.status }}
							</span>
						</td>
						<td class="px-4 py-3 text-center">
							<span
								class="material-icons text-gray-500 cursor-pointer hover:text-black"
							>
								tune
							</span>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

const searchQuery = ref('')
const filterDate = ref('')

const records = ref([
	{
		id: 'DR-2023-001',
		name: 'Robert Anderson',
		age: 78,
		date: '10/05/2023',
		cause: 'Natural causes',
		status: 'Verified',
	},
	{
		id: 'DR-2023-002',
		name: 'Eleanor Thompson',
		age: 85,
		date: '12/05/2023',
		cause: 'Heart failure',
		status: 'Pending',
	},
	{
		id: 'DR-2023-003',
		name: 'George Harris',
		age: 67,
		date: '15/05/2023',
		cause: 'Respiratory failure',
		status: 'Verified',
	},
	{
		id: 'DR-2023-004',
		name: 'Margaret Clark',
		age: 92,
		date: '18/05/2023',
		cause: 'Natural causes',
		status: 'Verified',
	},
	{
		id: 'DR-2023-005',
		name: 'Thomas Wright',
		age: 71,
		date: '20/05/2023',
		cause: 'Cardiac arrest',
		status: 'Pending',
	},
])

const filteredRecords = computed(() => {
	return records.value.filter((record) =>
		record.name.toLowerCase().includes(searchQuery.value.toLowerCase()),
	)
})
</script>

<style scoped>
.material-icons {
	font-size: 18px;
}
</style>
