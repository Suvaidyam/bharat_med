<template>
	<div class="p-6 min-h-screen">
		<!-- Header -->
		<div class="mb-6 flex items-center justify-between">
			<div>
				<h1 class="text-2xl font-bold">Birth Records</h1>
				<p class="text-sm text-gray-500">
					Manage and track all birth records in the system
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
						<th class="px-4 py-3">Child Name</th>
						<th class="px-4 py-3">Date of Birth</th>
						<th class="px-4 py-3">Parents</th>
						<th class="px-4 py-3">Attending Doctor</th>
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
						<td class="px-4 py-3">{{ record.child }}</td>
						<td class="px-4 py-3">{{ record.dob }}</td>
						<td class="px-4 py-3">{{ record.parents }}</td>
						<td class="px-4 py-3">{{ record.doctor }}</td>
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
		id: 'BR-2023-001',
		child: 'Emma Johnson',
		dob: '15/05/2023',
		parents: 'Sarah and Michael Johnson',
		doctor: 'Dr. Lisa Chen',
		status: 'Verified',
	},
	{
		id: 'BR-2023-002',
		child: 'Noah Williams',
		dob: '18/05/2023',
		parents: 'Jessica and David Williams',
		doctor: 'Dr. Robert Kim',
		status: 'Pending',
	},
	{
		id: 'BR-2023-003',
		child: 'Olivia Davis',
		dob: '20/05/2023',
		parents: 'Emily and James Davis',
		doctor: 'Dr. Lisa Chen',
		status: 'Verified',
	},
	{
		id: 'BR-2023-004',
		child: 'Liam Miller',
		dob: '22/05/2023',
		parents: 'Sophia and William Miller',
		doctor: 'Dr. John Smith',
		status: 'Verified',
	},
	{
		id: 'BR-2023-005',
		child: 'Ava Wilson',
		dob: '25/05/2023',
		parents: 'Olivia and Daniel Wilson',
		doctor: 'Dr. Robert Kim',
		status: 'Pending',
	},
])

const filteredRecords = computed(() => {
	return records.value.filter((record) =>
		record.child.toLowerCase().includes(searchQuery.value.toLowerCase()),
	)
})
</script>

<style scoped>
.material-icons {
	font-size: 18px;
}
</style>
